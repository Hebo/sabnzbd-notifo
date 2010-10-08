#!/usr/bin/env python
# Send download notifications from Sabnzbd to iPhone
import sys
import notifo

# Notifo API settings
USERNAME = "usernamehere"
API_KEY = "apikeyhere"


# Get NZB info
job = dict(name=sys.argv[3], status=int(sys.argv[7]))

if job['status'] == 0:
	job['long_status'] = "OK"
elif job['status'] == 1:
	job['long_status'] = "failed verification"
elif job['status'] == 2:
	job['long_status'] = "failed unpacking"
elif job['status'] == 3:
	job['long_status'] = "failed verification & unpacking"

if job['status'] == 0:
	print notifo.send_notification(USERNAME, API_KEY, USERNAME, 
									"{name} downloaded successfully".format(**job),
									"Sabnzbd", "Download Complete")
else:
	print notifo.send_notification(USERNAME, API_KEY, USERNAME, 
									"{name} {long_status}".format(**job),
									"Sabnzbd", "Download Failed")