import logging
from programmer import Programmer


class Scenario(object):
    def __init__(self):
        self.name = None
        self.binary_file_name = None

    def program(self):
        Programmer().program(self.binary_file_name)

    def run(self):
        log.info("Running Scenario: %s" % self.name)


log = logging.getLogger("{}.{}".format(Scenario.__module__, Scenario.__name__))
