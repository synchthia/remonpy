#!/usr/bin/env python3

import logging

class Controller:
    template = {}

    def __init__(self):
       logging.info("Controller Ensured...")

    def set(self, d: {}):
        data = {
            'operation': False
        }

        # Operation
        data['operation'] = d['operation']

        # Mode

        data['mode'] = d['mode']
