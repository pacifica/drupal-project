#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is an example CherryPy based event catch used in testing."""
import os
import io
import json
import cherrypy

# pylint: disable=too-few-public-methods
class Events(object):
    """Example root cherrypy class, method dispatcher required."""

    exposed = True

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    # pylint: disable=invalid-name
    # pylint: disable=no-self-use
    def POST(self, username):
        """Accept the post data and return it."""
        data = cherrypy.request.json
        print(data)
        return {'message': 'success'}

# pylint: disable=too-few-public-methods
class Root(object):
    """Example root cherrypy class, method dispatcher required."""

    exposed = True
    events = Events()


application = cherrypy.Application(Root(), '/', {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher()
    }
})

if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/', {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    })
