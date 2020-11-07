# This file is part of Linux Show Player
#
# Copyright 2020 Francesco Ceruti <ceppofrancy@gmail.com>
#
# Linux Show Player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linux Show Player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linux Show Player.  If not, see <http://www.gnu.org/licenses/>.

import logging

from lisp.core.configuration import DummyConfiguration

logger = logging.getLogger(__name__)


class PluginNotLoadedError(Exception):
    pass


# TODO: add possible additional metadata (Icon, Version, ...)
# TODO: implement some kind of plugin status
class Plugin:
    """Base class for plugins."""

    Name = "Plugin"
    Depends = ()
    OptDepends = ()
    Authors = ("None",)
    Description = "No Description"
    Config = DummyConfiguration()

    def __init__(self, app):
        """:type app: lisp.application.Application"""
        self.__app = app

    @property
    def app(self):
        """:rtype: lisp.application.Application"""
        return self.__app

    def finalize(self):
        """Called when the application is getting closed."""
