from fabric.api import cd, env, roles, task, run, sudo, local, lcd, settings


env.roledefs = {'production': ['ubuntu@ctflorals.com']}
env.forward_agent = True


@task
def sync():
    with lcd('./app'):
        local('python freeze.py')
    local('cp ./build/index.html ./www/views/index.html')
    local('cp ./build/about/index.html ./www/views/about.html')
    local('cp ./build/gallery/index.html ./www/views/gallery.html')
    local('cp ./build/testimonials/index.html ./www/views/testimonials.html')
    with settings(warn_only=True):
        local('git commit -am "prep for production deploy"')


@roles('production')
@task
def deploy():
    sync()
    with cd('/home/ctflorals/app'):
        sudo('chown -R ubuntu:ubuntu .')
        run('git pull')
        run('cp')
        run('sass --style compressed ./app/resources/css/src/styles.scss:./www/resources/css/styles.css')
        sudo('chown -R ctflorals:www-data .')

