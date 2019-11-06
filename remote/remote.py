#!/usr/bin/env python3

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

#    def ensureController(self, vendor: str, model: str):

