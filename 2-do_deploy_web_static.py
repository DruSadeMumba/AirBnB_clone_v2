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
        run(f"sudo tar -xzf /tmp/{file_name} -C {folder}")

        run(f"sudo rm -rf /tmp/{file_name}")
        run(f"sudo rsync -a --remove-source-files {folder}/web_static/* {folder}/")
        run(f"sudo rm -rf {folder}/web_static")
        run("sudo rm -rf /data/web_static/current")

        run(f"sudo ln -s {folder} /data/web_static/current")
        print("New version deployed!")
        return True

    except Exception:
        return False
