#!/usr/bin/env python3

import os
import pathlib
import logging
import web

# Logging
LOG_LEVEL = logging.INFO
if os.getenv("DEBUG", "") != "":
    LOG_LEVEL = logging.DEBUG

logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S %z',
        level=LOG_LEVEL
)

# Remote
from remote import remote

class RemonPi:
    path = str(pathlib.Path(__file__).resolve().parent)
    remote = None

    def __init__(self):
        logging.info(":: RemonPi Initialize...")

        # Vendor
        vendor = os.getenv('REMONPI_VENDOR')
        if vendor is None:
            raise Exception("REMONPI_VENDOR is not defined!")

        # Model
        model = os.getenv('REMONPI_MODEL')
        if model is None:
            raise Exception("REMONPI_MODEL is not defined!")

        logging.info(":: Vendor/Model choosed: %s/%s" % (vendor, model))

        # Remote
        self.remote = remote.Remote(self, vendor, model)

        # Web Server
        HTTP_PORT = os.getenv('HTTP_PORT')
        if HTTP_PORT is None:
            HTTP_PORT = 8080
        web.start(self, HTTP_PORT)

