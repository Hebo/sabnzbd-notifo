#!/usr/bin/env python
# Send test notification
import os

print "Sending test notification 1 of 2..."
os.system("python sabnzbd-notifo.py DLfolder linux.iso.nzb linux.iso 0 0 0 0")
print "Sending test notification 2 of 2..."
os.system("python sabnzbd-notifo.py DLfolder linux.iso.nzb linux.iso 0 0 0 3")
print "Done."