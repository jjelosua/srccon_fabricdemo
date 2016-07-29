from __future__ import with_statement
from fabric.api import *
import os

SERVER = os.environ.get('SERVER', 'hostname_or_ip_1')
SSH_USER = os.environ.get('SSH_USER', 'username')

# Setiting env
env.hosts = [SERVER]
env.user = SSH_USER


@task
def prepare_deploy():
    local("git add . && git commit")
    local("git push origin master")


@task
def deploy():
    code_dir = '/home/jjelosua/srccon/srccon_fabricdemo'
    with cd(code_dir):
        run("git pull origin master")


@task
def get_server_files():
    server_json_dir = '/home/jjelosua/srccon/json_files'
    with cd(server_json_dir):
        with lcd('data'):
            get('*.json', '.')
