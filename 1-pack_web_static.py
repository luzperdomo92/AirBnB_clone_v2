#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


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
