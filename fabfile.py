from fabric.api import local, cd, run, env

env.hosts = ['jsietsma@jsietsma.webfactional.com']

def local_run_tests():
    local('./manage.py test corpseflipper')

def local_push_code():
    local('git push')

def remote_pull_source():
    with cd('/home/jsietsma/webapps/django13/corpse/'):
        run('git pull')

def remote_restart_server():
    run('/home/jsietsma/webapps/django13/apache2/bin/restart')

def remote_run_tests():
    _remote_manage_command('test corpseflipper')

def remote_validate_models():
    _remote_manage_command('validate')

def remote_syncdb():
    _remote_manage_command('syncdb')

def remote_migrate():
    _remote_manage_command('migrate corpseflipper')

def _remote_manage_command(cmd ):
    with cd('/home/jsietsma/webapps/django13/corpse/'):
        run('python2.7 manage.py %s' % cmd)

def deploy():
    local_run_tests()
    local_push_code()
    remote_pull_source()
    remote_run_tests()
    remote_validate_models()
    #remote_migrate()
    remote_restart_server()

def deploy_media():
    local_push_code()
    remote_pull_source()
