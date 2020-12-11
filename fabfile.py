#from fabric.api import env, run, local
from fabric.api import local
import os, sys

#machine=input("machine: ")

#env.hosts = [ '192.168.1.100', '192.168.1.101', '192.168.1.102' ]

#env.hosts = [ machine ]
'''
from invoke import Responder

git_watchers = [
                Responder(pattern = r"Username for .*", response="lewis.machilika@nbs.mw\n"), 
                Responder(pattern = r"Password for .*", response="#include<iostream>1993\n")
               ]

local("git fetch", watchers=git_watchers)
'''
import datetime

now = datetime.datetime.now()

import zipfile

def zipdir(path, ziph):
    
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def test():
    local("./manage.py test my_app")

def commit():

    val=input(" Enter your commit :")
    
    local("git add . && git commit -m \"{0}\"".format(val))

def clone():
    
    local("git init && git clone https://github.com/lewisMachilika/screeenshot.git")
    
    local("cd screeenshot && Rmdir /S .git && cd ../")
    
    bkp="screeenshot{0}".format(now.strftime("-%Y-%m-%d-%H%M%S"))
    
    os.rename("screeenshot",bkp)

    zipf = zipfile.ZipFile('../{0}.zip'.format(bkp), 'w', zipfile.ZIP_DEFLATED)
    
    zipdir(bkp, zipf)
    
    zipf.close()

    local("Rmdir /S {0}".format(bkp))

def push():
    local("git push")

def pull():
    local("git pull")

def prepare_deploy():
    #test()
    commit()
    push()

def commit_push():
    name=input("Enter your full name :")
    task=input("What are you doing")
    local("git add . && git commit -m \"{0}\" && git push".format(name +' '+task+' '+ now.strftime("-%Y-%m-%d %H:%M:%S ")))
    
def directory():
  local('dir')