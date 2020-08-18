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
    release_path = "/data/web_static/releases/%s" % (file_name_wo_ext)

    try:
        put(archive_path, '/tmp/%s' % (file_name))
        run("mkdir -p %s" % (release_path))
        run("tar -xzf /tmp/%s -C %s/" % (file_name, release_path))
        run("rm /tmp/%s" % (file_name))
        run("mv %s/web_static/* %s/" % (release_path, release_path))
        run("rm -rf %s/web_static" % (release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s %s /data/web_static/current" % (release_path))
        return True
    except:
        return False
