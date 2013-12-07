Psistats Linux Client
=====================

Version: 0.0.2
--------------

Python linux client that sends some computer statistics to a RabbitMQ
server.

Installation
------------

Requires the following python dependencies:

pika
simplejson
netifaces
psutil

Init Script
-----------

1. Copy psistats-service to /etc/init.d/psistats-service
2. Edit the file to make sure it can find the psistats python script
3. Run update-rc.d psistats-service defaults
4. Start psistats: /etc/init.d/psistats-service start
 
