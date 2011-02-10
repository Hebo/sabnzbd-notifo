sabnzbd-notifo.py
=================

Introduction
------------
sabnzbd-notifo.py is a sabnzbd post-processing script that allows you to send download notifications from Sabnzbd to the Notifo service, which can forward notifications to iOS devices.


Usage
-----

### Setup ###
Make sure you have a Notifo account first!

### Linux / OSX ###
1.  Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > Folders) to the folder containing this script
2.  Set the default user script (in Settings > Switches) to _sabnzbd-notifo.py_
3.  In sabnzbd-notifo.py, enter in your Notifo _username_ and _api secret_

### Windows ###
1.  Install [Python 2.7](http://www.python.org/download/releases/2.7.1/) and [py2exe](http://www.py2exe.org/) for python 2.7
2.  In sabnzbd-notifo.py, enter in your Notifo _username_ and _api secret_
3.  Run the command `python py2exe-setup.py py2exe` to create an exe
4.  Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > Folders) to the folder containing the exe (/dist/)
5.  In Sabnzbd Settings > Switches, set "Default User Script" to sabnzbd-notifo.exe