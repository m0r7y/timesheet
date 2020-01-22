import sys
import xmlrpclib
from datetime import datetime
from random import choice
from urlparse import urljoin


class SockXml(object):
    def __init__(self, username, pwd, dbname, url):
        self.username = username
        self.pwd = pwd
        self.dbname = dbname
        self.url = url

    def execute(self, work):
        try:
            sock_common = xmlrpclib.ServerProxy(urljoin(self.url, "/xmlrpc/common"))
            uid = sock_common.login(self.dbname, self.username, self.pwd)
            sock = xmlrpclib.ServerProxy(urljoin(self.url, "/xmlrpc/object"))
            sock.execute(self.dbname, uid, self.pwd, 'project.task.work', 'create', work)
        except Exception:
            print"failed"


if __name__ == "__main__":
    username = ''
    password = ''
    dbname = 'ingenosya_business_service'
    url = 'http://192.168.200.209:8067'
    # tasks that you "have done" today :D
    tasks = [
        u'Maintenance et mise a jour serveur',
        u'Implementation d\'algorithme de filtre pour le modele \"training.session\"',
        u'Tests des backups',
        u'Creation de modele pour le backend',
        u'Creation de snippets dynamique',
        u'Amelioration du code jquery du site'
    ]

    work = {
        'name': choice(tasks),
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'task_id': 8548,  # my task_id
        'hours': 8.0,  # always 8 hours lol
        'user_id': 352,  # me
        'company_id': 1,  # ingenosya res.company.id
    }

    SockXml = SockXml(username, password, dbname, url)
    work_id = SockXml.execute(work)
