#!/usr/bin/env python3

import sys

# mitsubishi
import controller.mitsubishi.kgsa3c.controller as kgsa3c

class Remote:
    app = None
    vendor = ""
    model = ""

    controller = None

    def __init__(self, app, vendor, model):
        self.app = app
        self.vendor = vendor
        self.model = model

        self.ensureController(vendor, model)

    def ensureController(self, vendor: str, model: str):
        """ ensureController - Choose Controller from vendor/model. """
        if vendor == "mitsubishi" and model == "kgsa3-c":
            self.controller = kgsa3c.Controller()
