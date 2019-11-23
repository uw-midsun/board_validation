import logging
from scenarios.scenario import Scenario


class TutorialBoardButtonInterrupt(Scenario):
    def __init__(self):
        super().__init__()
        self.name = 'Tutorial Board: Button Press'
        self.binary_file_name = 'tutorial_board_button_interrupt.bin'
        self.description = 'In this scenario, pressing switch 1 (green) will toggle LED 1 (blue) on the tutorial ' \
                           'board, and pressing switch 2 (yellow) will toggle LED 2 (yellow)'

    def run(self):
        super().run()
        log.info(self.description)
        self.program()
        log.info("Press any key to continue.")
        input()


log = logging.getLogger()
