#!/usr/bin/env python3

import json
import logging
import tornado.ioloop
import tornado.web

class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(
            status_code=404,
            reason="Not Found"
        )

    def write_error(self, status_code, exc_info=None, **kwargs):
        self.finish({"error": self._reason})

class RemoteHandler(tornado.web.RequestHandler):
    def initialize(self, app):
        self.app = app

    def post(self):
        try:
            req = tornado.escape.json_decode(self.request.body)
            res = json.dumps(req, ensure_ascii=False)
            self.write(res)
        except json.decoder.JSONDecodeError as ex:
            raise tornado.web.HTTPError(
                status_code=400,
                reason="Failed decode json"
            )

    def write_error(self, status_code, exc_info=None, **kwargs):
        self.finish({"error": self._reason})

def start(app, port: int):
    web = tornado.web.Application([
        (r"/api/v1/remote", RemoteHandler, dict(app=app)),
    ], default_handler_class=DefaultHandler)

    web.listen(port)
    logging.info("HTTP Server started on %d", port)

    tornado.ioloop.IOLoop.current().start()
