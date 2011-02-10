sabnzbd-notifo.py
=================

Introduction
------------
sabnzbd-notifo.py is a sabnzbd post-processing script that allows you to send download notifications from Sabnzbd to the Notifo service, which can forward notifications to iOS devices.


Usage
-----

Make sure you have a Notifo account first!

### Linux / OSX ###
1. Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > General) to the folder containing this script
2. Set the default user script (in Settings > Switches) to _sabnzbd-notifo.py_
3. In sabnzbd-notifo.py, enter in your Notifo _username_ and _api secret_

### Windows ###
1. In sabnzbd-notifo.py, enter in your Notifo _username_ and _api secret_
2. Install [py2exe](http://www.py2exe.org/)
2. Run the command `python py2exe-setup.py py2exe` to create exe
3. Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > General) to the folder containing the exe (/dist/)