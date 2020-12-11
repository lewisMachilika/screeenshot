#from fabric.api import env, run, local
from fabric.api import local

#machine=input("machine: ")

#env.hosts = [ '192.168.1.100', '192.168.1.101', '192.168.1.102' ]

#env.hosts = [ machine ]

def test():
    local("./manage.py test my_app")

def commit():

    val=input(" Enter your commit :")
    local("git add . && git commit -m '{0}'".format(val))

def push():
    local("git push")

def prepare_deploy():
    #test()
    commit()
    push()

def commit_push():
    val=input("CP Enter your commit :")
    local("git add . && git commit -m \"{0}\" ".format(val))
    local("git push")
def directory():
  local('dir')