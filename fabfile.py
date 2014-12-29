from __future__ import unicode_literals

import os
from collections import namedtuple
from fabric.api import cd, run, sudo, task
from fabric.contrib.files import append, exists, is_link


__all__ = ['VAGRANT_DIRECTORY',
           'HOME_DIRECTORY',
           'BASH_PROFILE_FILE',
           'SCRIPTS_DIRECTORY',
           'STORAGE_DIRECTORY',
           'REQUIRED_DEBIAN_PACKAGES',
           'SOFTWARES_URLS',
           'SCRIPTS',
           'INTERPRETERS',
           'REQUIRED_PYTHON_PACKAGES',
           'WORKSPACE_DIRECTORY',
           'Repository',
           'REPOSITORIES',
           'WEBSITE_LOCAL_DIRECTORY',
           'download',
           'system_update',
           'install_required_packages',
           'install_anaconda',
           'create_bash_profile_file',
           'source_bash_profile_file',
           'create_environments',
           'clone_repositories',
           'configure_website']

VAGRANT_DIRECTORY = '/vagrant'
HOME_DIRECTORY = '/home/vagrant'
SCRIPTS_DIRECTORY = os.path.join(VAGRANT_DIRECTORY, 'scripts')
STORAGE_DIRECTORY = os.path.join(VAGRANT_DIRECTORY, 'tmp')

BASH_PROFILE_FILE = os.path.join(HOME_DIRECTORY, '.bash_profile')

REQUIRED_DEBIAN_PACKAGES = [
    'expect',
    'fontconfig',
    'git',
    'libsm6',
    'libxrender-dev',
    'wget']

SOFTWARES_URLS = {
        'anaconda': 'http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-2.0.1-Linux-x86_64.sh'}  # noqa

SCRIPTS = {
    'anaconda_expect': os.path.join(SCRIPTS_DIRECTORY, 'anaconda_expect.exp')
}

INTERPRETERS = {
    'python2.7': '2.7',
}

REQUIRED_PYTHON_PACKAGES = [
    'backports.functools_lru_cache',
    'coverage',
    'flake8',
    'sphinx_bootstrap_theme',
    'sphinxcontrib-napoleon'
]



def download(url, directory):
    """
    Downloads given url to given directory.
    Parameters
    ----------
    url : unicode
        Url to download.
    directory : unicode
        Directory to write the download to.
    """

    run('wget -P {0} {1}'.format(directory, url))


@task
def system_update():
    """
    Task for system update.
    """

    sudo('apt-get update --yes')


@task
def install_required_packages(required_packages=REQUIRED_DEBIAN_PACKAGES):
    """
    Task for required packages installation.
    Parameters
    ----------
    required_packages : array_like
        Required system packages to install.
    """

    for package in required_packages:
        sudo('apt-get install --yes {0}'.format(package))


@task
def install_anaconda(url=SOFTWARES_URLS.get('anaconda'),
                     directory=STORAGE_DIRECTORY,
                     anaconda_expect_script=SCRIPTS.get('anaconda_expect')):
    """
    Task for *Anaconda* installation.
    Parameters
    ----------
    url : unicode
        *Anaconda* installer url.
    directory : unicode
        Directory to write the download to.
    anaconda_expect_script : unicode
        *Anaconda* *expect* installation script.
    """

    anaconda_installation_directory = os.path.join(HOME_DIRECTORY, 'anaconda')
    if not exists(anaconda_installation_directory):
        name = os.path.basename(url)
        anaconda_installer = os.path.join(directory, name)
        if not exists(anaconda_installer):
            download(url, directory)

        run('chmod +x {0}'.format(anaconda_installer))
        run('chmod +x {0}'.format(anaconda_expect_script))
        run('expect {0} {1}'.format(
            anaconda_expect_script, anaconda_installer))

