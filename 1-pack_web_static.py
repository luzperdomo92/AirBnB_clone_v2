#!/usr/bin/python3
from fabric.api import run, local
from datetime import date


def do_pack():
    """packs the content of web_static"""

    folder_name = "web_static"
    today = date.today()
    today_str = today.strftime("%Y%m%d%l%M%S")
    file_name = "%s_%s.tgz" % (folder_name, today_str)
    file_path = "versions/%s" % (file_name)

    result = local("mkdir -p versions")
    if result.failed:
        return None
    result = local("tar -cvzf %s %s" % (file_path, folder_name))
    if result.failed:
        return None
    return file_path
