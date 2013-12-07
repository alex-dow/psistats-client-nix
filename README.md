Psistats Linux Client v0.0.1

Python dependencies:
pika
simplejson
netifaces
psutil

Init Script:

1. Copy psistats-service to /etc/init.d/psistats-service
2. Edit the file to make sure it can find the psistats python script
3. Run update-rc.d psistats-service defaults
4. Start psistats: /etc/init.d/psistats-service start
 
