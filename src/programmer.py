import logging
import os
from sys import platform


class Programmer(object):
    IMAGES_DIR = 'images'

    def __init__(self):
        if platform == "linux" or platform == "linux2":
            self.OPEN_OCD = '/usr/bin/openocd'
        elif platform == "darwin":
            self.OPEN_OCD = '/usr/local/bin/openocd'
        self.OPEN_OCD_COMMAND = '%s  -f interface/cmsis-dap.cfg -f target/stm32f0x.cfg -f ' \
                                'openocd_scripts/stm32f0-openocd.cfg -c "stm_flash %s" -c shutdown' \
                                '2> /dev/null' % (self.OPEN_OCD, '%s')

    def _make_cmd(self, path):
        before = "/usr/local/bin/openocd -f interface/cmsis-dap.cfg -f target/stm32f0x.cfg -f " \
               "openocd_scripts/stm32f0-openocd.cfg -c"
        command = "stm_flash %s" % path
        after = "-c shutdown 2> /dev/null"
        return before.split() + [command] + after.split()

    def program(self, image_name):
        image_path = '{}/{}'.format(Programmer.IMAGES_DIR, image_name)
        log.info("Beginning programming: %s onto the board" % image_path)
        command_string = self.OPEN_OCD_COMMAND % image_path + " 2>&1 > /dev/null"
        os.system(command_string)
        log.info("Programming done!")


log = logging.getLogger("{}.{}".format(Programmer.__module__, Programmer.__name__))
