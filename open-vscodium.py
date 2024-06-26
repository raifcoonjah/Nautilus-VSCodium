#!/usr/bin/env python3

import os

# A way to get unquote working with python 2 and 3
try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

import gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject


class OpenVSCodiumExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass
        # self.client = GConf.Client.get_default()
        
    def _open_vscodium(self, file):
        filename = unquote(file.get_uri()[7:])

        os.chdir(filename)
        os.system('codium .')
        
    def menu_activate_cb(self, menu, file):
        self._open_vscodium(file)
        
    def menu_background_activate_cb(self, menu, file): 
        self._open_vscodium(file)
       
    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]
        if not file.is_directory() or file.get_uri_scheme() != 'file':
            return
       
        item = Nautilus.MenuItem(name='NautilusPython::openvscodium_file_item',
                                 label='Open in VSCodium' ,
                                 tip='Open %s in VSCodium' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return item,

    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(name='NautilusPython::openvscodium_file_item2',
                                 label='Open in VSCodium' ,
                                 tip='Open %s in VSCodium' % file.get_name())
        item.connect('activate', self.menu_background_activate_cb, file)
        return item,