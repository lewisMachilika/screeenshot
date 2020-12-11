from fabric.api import local

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