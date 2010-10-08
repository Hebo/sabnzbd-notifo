# Create windows exe with py2exe using the command 
# python py2exe-setup.py py2exe
from distutils.core import setup
import py2exe

setup(console=['sabnzbd-notifo.py'])