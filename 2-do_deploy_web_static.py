#!/usr/bin/python3
"""2-do_deploy_web_static"""
from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = [
    '35.243.241.181',
    '3.87.74.240'
]


def do_deploy(archive_path):
    """ Do Deploy """
    # check the file if exits
    if not os.path.exists(archive_path):
        return False

    # web_static_20170315003959.tgz
    file_name = archive_path.split("/")[-1]
    # web_static_20170315003959
    file_name_wo_ext = file_name.split(".")[0]
    release_path = "/data/web_static/releases/{}".format(file_name_wo_ext)

    try:
        put(archive_path, '/tmp')
        run("mkdir -p {}/".format(release_path))
        run("tar -xzf /tmp/{} -C {}/".format(file_name, release_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(release_path))
        return True
    except:
        return False
