#!/usr/bin/env python
from os import environ as env
import sys

if __name__ == "__main__":

    test_command = filter(lambda x: x == "test", sys.argv)
    environment = "test" if test_command else "local"
    settings = "config.settings.%s" % environment
    env.setdefault("DJANGO_SETTINGS_MODULE", settings)

    print("Running with %s" % settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
