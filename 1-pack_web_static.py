#!/usr/bin/python3
from fabric.api import run
from datetime import date


def do_pack():
    """packs the content of web_static"""

    folder_name = "web_static"
    today = date.today()
    today_str = today.strftime("%Y%m%d%l%M%S")
    run("mkdir versions")
    run("tar -cvzf versions/%s_%s.tgz %s" % (folder_name, today_str,
                                             folder_name))
