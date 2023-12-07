#!/usr/bin/python3
"""Full deployment"""
from datetime import datetime
from os.path import exists
from fabric.api import env, put, run, local

env.hosts = ['52.204.67.182', '18.209.180.1']


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


def do_deploy(archive_path):
    """Deploy archive"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        folder = f'/data/web_static/releases/{file_name.split(".")[0]}'

        run(f"mkdir -p {folder}")
        run(f"tar -xzf /tmp/{file_name} -C {folder}")

        run(f"rm -rf /tmp/{file_name}")
        run(f"mv {folder}/web_static/* {folder}/")
        run(f"rm -rf {folder}/web_static")
        run("rm -rf /data/web_static/current")

        run(f"ln -s {folder} /data/web_static/current")
        return True

    except Exception:
        return False


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
