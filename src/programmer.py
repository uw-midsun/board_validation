import logging
import os
import subprocess
from subprocess import CalledProcessError
from sys import platform

from exceptions import BinaryDoesntExist, ProgrammerNotConnected
from util.file_utilities import ensure_path_exists


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

    def _get_img_path(self, image):
        return "{}/{}".format(self.IMAGES_DIR, image)


    def _make_cmd(self, path):
        before = "/usr/local/bin/openocd -f interface/cmsis-dap.cfg -f target/stm32f0x.cfg -f " \
               "openocd_scripts/stm32f0-openocd.cfg -c"
        command = "stm_flash %s" % path
        after = "-c shutdown 2> /dev/null"
        return before.split() + [command] + after.split()

    def run_openocd(self, img_path):
        try:
            command = [
                self.OPEN_OCD,
                "-f", "interface/cmsis-dap.cfg",
                "-f", "target/stm32f0x.cfg",
                "-f", "openocd_scripts/stm32f0-openocd.cfg",
                "-c", "stm_flash {}".format(img_path), "-c", "shutdown"
            ]
            log.debug(" ".join(command))
            subprocess.run(command, check=True)
        except CalledProcessError as e:
            raise ProgrammerNotConnected from e

    def program(self, image_name):
        img_path = self._get_img_path(image_name)
        if not ensure_path_exists(img_path):
            raise BinaryDoesntExist()
        image_path = '{}/{}'.format(Programmer.IMAGES_DIR, image_name)
        log.info("Beginning programming: %s onto the board" % image_path)
        programming_done = False
        while not programming_done:
            try:
                self.run_openocd(img_path)
                programming_done = True
            except ProgrammerNotConnected:
                log.error("Error finding the device, please check your "
                          "connections and try again! Hit enter when done.")
                input()
        log.info("Programming done!")


log = logging.getLogger("{}.{}".format(Programmer.__module__, Programmer.__name__))
