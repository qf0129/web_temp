import os
from web.settings import *
DEBUG = True

class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return 'notmigrations'

MIGRATION_MODULES = DisableMigrations()
