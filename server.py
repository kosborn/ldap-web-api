from flask import Flask
import ldap3, re
import config

server = ldap3.Server(config.ldap['domain'], get_info=ldap3.ALL)
conn = ldap3.Connection(server, config.ldap['username'], config.ldap['password'], auto_bind=True)

app = Flask(__name__)


@app.route('/')
def hello():
    return ""

@app.route('/ldap/objectGUID/<guid>')
def guid(guid):
    try:
        if not re.match('^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$',guid):
            match = re.search('([0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12})',guid)
            if not match:
                return "bad guid", 500
            guid = match.group(0)
        if conn.search('<GUID=%s>' % guid,'(objectGUID=*)', attributes=ldap3.ALL_ATTRIBUTES):
            return conn.entries[0].entry_to_json()
        else:
            return "GUID not found", 404
    except Exception as e:
        print(e)
        return "none found", 404

@app.route('/ldap/objectSid/<sid>')
def sid(sid):
    try:
        if not re.match('^S-\d-(\d+-){1,14}\d+$',sid):
            return "bad sid", 500
        if conn.search(conf.ldap['baseDN'],'(objectSid=%s)' % sid, attributes=ldap3.ALL_ATTRIBUTES):
            return conn.entries[0].entry_to_json()
    except:
        return "none found", 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)

