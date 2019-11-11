import logging
from scenarios.scenario import Scenario


class BlinkingLed(Scenario):
    def __init__(self):
        super().__init__()
        self.name = 'Blinking LEDs'
        self.binary_file_name = 'controller_board_blinking_leds.bin'
        self.description = 'This scenario blinks the LEDs on the controller board.\n' \
                           'Note that there are 4 LEDs on the controller board:\n' \
                           '\tPA15 - Blue\n' \
                           '\tPB3 - Red\n' \
                           '\tPB4 - Yellow\n' \
                           '\tPB5 - Green\n'

    def run(self):
        super().run()
        log.info(self.description)
        self.program()
        log.info("Press any key to continue.")
        input()


log = logging.getLogger("{}.{}".format(BlinkingLed.__module__, BlinkingLed.__name__))
