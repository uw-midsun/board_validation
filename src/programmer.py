import logging
import os


class Programmer(object):
    IMAGES_DIR = 'images'
    OPEN_OCD = '/usr/local/bin/openocd'
    OPEN_OCD_COMMAND = '%s  -f interface/cmsis-dap.cfg -f target/stm32f0x.cfg -f ' \
                       'openocd_scripts/stm32f0-openocd.cfg -c "stm_flash %s" -c shutdown' \
                       '2> /dev/null' % (OPEN_OCD, '%s')

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
