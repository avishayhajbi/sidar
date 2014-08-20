from fabric.api import *


env.hosts = ['sidar@10.0.10.4']
DESIGN26_HOSTNAME = 'design26.local'
github_repo = 'https://github.com/danielbraun/sidar.git'
#github_repo = 'https://github.com/avishayhajbi/sidar.git'
design26m_mount_point = '/mnt/design26m'
source = 'source bin/activate && '


def mount_design26m():
    from socket import gethostbyname, gaierror
    try:
        design26_ip = gethostbyname(DESIGN26_HOSTNAME)
    except gaierror:
        raise Exception('Could not reach design26 - Is it on? Are you connected to Shenkar network?')
    sudo('if mount | grep design26m; then umount %s; fi;' % design26m_mount_point)
    sudo('mkdir -p %s' % design26m_mount_point)
    sudo('if ! mount | grep design26m; then mount.cifs //%s/M$ %s -o user=sidar; fi;' % (design26_ip, design26m_mount_point))


def import_sidar_mysql():
    mount_design26m()
    run('mysql -u root < %s' % design26m_mount_point + '/shenkar-php/sidar.sql')


def push_ssh_key():
    """Pushes SSH key to remote host, so password won't have to be entered each time"""
    keyfile = '/tmp/%s.pub' % env.user
    run('mkdir -p ~/.ssh && chmod 700 ~/.ssh')
    put('~/.ssh/id_rsa.pub', keyfile)
    run('cat %s >> ~/.ssh/authorized_keys' % keyfile)
    run('rm %s' % keyfile)


def deploy_shenkar_server():
    with cd('~/django_projects/sidar'):
        run('git pull')
        run(source + 'pip install -r requirements/common.txt')
        run(source + 'python manage.py migrate')
        run(source + 'python manage.py collectstatic --noinput')
    sudo('service sidar restart')


def test():
    local('./manage.py test backoffice bibliography collection feedback timeline links articles videos')


def deploy():
    test()
    local('git push origin master')
    local('git push heroku master')
    local('heroku open')
