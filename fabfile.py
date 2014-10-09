from fabric.api import *


env.hosts = ['172.19.3.123']
env.user = 'xin'
env.password = '1201027'


def add():
    local("git add .")


def commit():
    local("git commit -a ")


def push():
    local("git push")


def pull():
    local("git pull")


def clone():
    code_dir = '/home/xin/www'
    with cd(code_dir):
        run("git clone https://github.com/defshine/flaskblog.git")


def deploy():
    code_dir = '/home/xin/www/flaskblog'
    with cd(code_dir):
        run("git pull")
        run("gunicorn -b 0.0.0.0:8005 run:app")