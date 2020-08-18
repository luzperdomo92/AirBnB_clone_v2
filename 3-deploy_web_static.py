#!/usr/bin/python3
"""2-do_deploy_web_static"""
from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = [
    '35.243.241.181',
    '3.87.74.240'
]


def deploy():
    """ do_pack and then do_deploy with file created"""
    name = do_pack()
    if not name:
        return False

    return do_deploy("versions/{}".format(name))


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
