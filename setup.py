try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
 'description':'Stocks',
 'author':'Omar El-Mohri',
 'url':'ipconnex.com',
 'download_url':'ipconnex.com',
 'author_email':'omarelmohri@ipconnex.com',
 'version':'0.1',
 'install_requires':['nose'],
 'packages':['Stocks'],
 'scripts':[],
 'name':'Stocks'
}

setup(**config)
