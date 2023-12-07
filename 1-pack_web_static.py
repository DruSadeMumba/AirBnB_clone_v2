#!/usr/bin/python3
"""Compress before sending"""
from datetime import datetime
from os.path import exists
from fabric.api import local
import tarfile


def do_pack():
    """Compress before sending"""
    if not exists("versions"):
        local("mkdir -p versions")

    t_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{t_time}.tgz"
    try:
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception:
        return None
