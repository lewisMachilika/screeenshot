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

os.rename("myfolder","myfolder{0}".format(now.strftime("-%Y-%m-%d-%H%M%S")))
def test():
    local("./manage.py test my_app")

def commit():

    val=input(" Enter your commit :")
    local("git add . && git commit -m \"{0}\"".format(val))

def push():
    local("git push")

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