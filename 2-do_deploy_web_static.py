#!/usr/bin/python3
from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = [
    '35.243.241.181',
    '3.87.74.240'
]


def do_pack():
    """packs the content of web_static"""

    folder_name = "web_static"
    now = datetime.now()
    today_str = now.strftime("%Y%m%d%H%M%S")
    file_name = "%s_%s.tgz" % (folder_name, today_str)
    file_path = "versions/%s" % (file_name)

    result = local("mkdir -p versions")
    if result.failed:
        return None
    result = local("tar -cvzf %s %s" % (file_path, folder_name))
    if result.failed:
        return None
    return file_name


def do_deploy(archive_path):
    """ Do Deploy """
    # check the file if exits
    if not os.path.exists(archive_path):
        return False

    # web_static_20170315003959.tgz
    file_name = os.path.basename(archive_path)
    # web_static_20170315003959
    file_name_wo_ext = os.path.splitext(file_name)[0]

    rs = put(archive_path, '/tmp/%s' % (file_name))
    if rs.failed:
        return False
    rs = run("mkdir -p /data/web_static/releases/%s" % (file_name_wo_ext))
    if rs.failed:
        return False

    rs = run("tar -xzf /tmp/%s -C /data/web_static/releases/%s/" % (
        file_name, file_name_wo_ext))
    if rs.failed:
        return False

    rs = run("rm /tmp/%s" % (file_name))
    if rs.failed:
        return False
    rs = run("mv /data/web_static/releases/%s/web_static/* \
        /data/web_static/releases/%s/" % (file_name_wo_ext, file_name_wo_ext))
    if rs.failed:
        return False
    rs = run("rm -rf /data/web_static/releases/%s/web_static" % (
        file_name_wo_ext))
    if rs.failed:
        return False

    rs = run("rm -rf /data/web_static/current")
    if rs.failed:
        return False
    rs = run("ln -s /data/web_static/releases/%s/ \
             /data/web_static/current" % (file_name_wo_ext))
    if rs.failed:
        return False

    return True
