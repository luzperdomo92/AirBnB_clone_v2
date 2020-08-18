#!/usr/bin/python3
from fabric.api import run, local
from datetime import date


def do_pack():
    """packs the content of web_static"""

    folder_name = "web_static"
    today = date.today()
    today_str = today.strftime("%Y%m%d%l%M%S")
    file_name = "%s_%s.tgz" % (folder_name, today_str)

    local("mkdir -p versions")
    local("tar -cvzf versions/%s %s" % (file_name, folder_name))
    return file_name
