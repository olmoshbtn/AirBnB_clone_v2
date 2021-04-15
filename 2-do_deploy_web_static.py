#!/usr/bin/python3
"""
Fabric script to generate a .tgz from web_static folder
and upload the new web_static to web servers
"""
from fabric.api import *
import datetime
import os.path


env.hosts = ['34.75.15.109', '35.227.52.42']
env.user = 'ubuntu'


def do_pack():
    """
    Compress the content of web_static folder in a .tgz
    """
    now = datetime.datetime.now()
    str_time = now.strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}".format(str_time)
    local("mkdir -p versions")
    status_f = local("tar -cvzf versions/{}.tgz web_static".format(file_name))

    if status_f.succeeded:
        return "versions/{}.tzg".format(file_name)
    else:
        return None


def do_deploy(archive_path):
    """
    Deploy the file to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path[9:]
        file_name_no_ext = archive_path[9:-4]
        abs_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}{}/".format(abs_path, file_name_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/"
            .format(file_name, abs_path, file_name_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {}{}/web_static/* {}{}/"
            .format(abs_path, file_name_no_ext, abs_path, file_name_no_ext))
        run("rm -rf {}{}/web_static".format(abs_path, file_name_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current"
            .format(abs_path, file_name_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
