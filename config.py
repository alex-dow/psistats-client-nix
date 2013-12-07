###############################################################################
# Psistats Configuration                                                      #
#                                                                             #
# Version 0.0.1                                                               #
# MIT License                                                                 #
# v0idnull                                                                    #
# http://www.psikon.com/                                                      #
###############################################################################
import sys
import logging.handlers
import logging
###
# SERVER SETTINGS
#
# Settings for RabbitMQ Server
###
SERVER_HOST = "localhost"
SERVER_PORT = 5672
SERVER_USERNAME = "guest"
SERVER_PASSWORD = "guest"
SERVER_RETRY_DELAY = 5

###
# EXCHANGE SETTINGS
#
# If the exchange already exists in your RabbitMQ server,
# then the settings here must be identical to the settings
# of the existing exchange
###
EXCHANGE_NAME       = "psistats"
EXCHANGE_TYPE       = "topic"
EXCHANGE_DURABLE    = False
EXCHANGE_AUTODELETE = False
EXCHANGE_OPTIONS    = None

###
# QUEUE SETTINGS
#
# If the queue already exists in your RabbitMQ server,
# then the settings here must be identical to the settings
# of the existing queue.
###
QUEUE_NAME          = "psistats-compname"
QUEUE_EXCLUSIVE     = False
QUEUE_DURABLE       = False
QUEUE_AUTODELETE    = True
QUEUE_ROUTINGKEY    = "psistats-compname"
QUEUE_OPTIONS       = {"x-message-ttl": 10000}

###
# LOGGING SETTINGS
###
LOG_FILE            = "/var/log/psistats.log"
LOG_LEVEL           = logging.DEBUG
LOG_HANDLERS        = [ logging.StreamHandler(sys.stdout), 
                        logging.handlers.TimedRotatingFileHandler(LOG_FILE,
                            when='midnight',
                            backupCount=5
                      )]

###
# MISC APPLICATION SETTINGS
###
TIMER               = 1
QUEUE_DECLARE_TIMER = 60
WORKING_DIR         = "."
