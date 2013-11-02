"""Base class for apitools proxy servers."""

import abc
import re

import webapp2

class Error(Exception):
  """Base error for apitools proxy."""


class BaseApiProxyApp(webapp2.WSGIApplication):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def __init__(self):
    """Create a BaseApiProxyApp."""
    self.__route_table = {}

  @property
  def app(self):
    app = webapp2.WSGIApplication(self.Routes(), debug=True)
    return app

  def _AddRoute(self, path, method):
    if path in self.__route_table:
      raise Error('Redefining route for path %s' % path)
    if re.match('/.+/.+', path) is None:
      raise Error('Invalid path: %s' % path)
    self.__route_table[path] = method

  def Routes(self):
    return self.__route_table.iteritems()
