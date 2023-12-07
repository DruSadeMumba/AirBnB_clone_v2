#!/usr/bin/python3
"""Deploy archive"""
from os.path import exists
from fabric.api import env, put, run

env.hosts = ['52.204.67.182', '18.209.180.1']


def do_deploy(archive_path):
    """Deploy archive"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        folder = f'/data/web_static/releases/{file_name.split(".")[0]}'

        run(f"sudo mkdir -p {folder}")
        run(f"tar -xzf /tmp/{file_name} -C {folder}")

        run(f"rm -rf /tmp/{file_name}")
        run(f"mv {folder}/web_static/* {folder}/")
        run(f"rm -rf {folder}/web_static")
        run("rm -rf /data/web_static/current")

        run(f"ln -s {folder} /data/web_static/current")
        return True

    except Exception:
        return False
