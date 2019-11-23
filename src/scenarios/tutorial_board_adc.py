import logging
import sys
import threading
from queue import Queue
from controller_board.uart_driver import UartDriver
from scenarios.scenario import Scenario


class TutorialBoardAdc(Scenario):
    def __init__(self):
        super().__init__()
        self.name = 'Tutorial Board: ADC'
        self.binary_file_name = 'tutorial_board_adc.bin'
        self.description = 'In this scenario, adc values on the potentiometer are read and shown, change the value on' \
                           'the potentiometer and make sure the values change'
        self.keyboard_queue = Queue()
        self.input_thread = None
        self.thread_running = None

    def add_input(self, input_queue):
        while self.thread_running:
            input_queue.put(sys.stdin.read(1))

    def setup(self):
        self.input_thread = threading.Thread(target=self.add_input, args=(self.keyboard_queue,))
        self.input_thread.daemon = True
        self.thread_running = True
        self.input_thread.start()

    def get_keyboard_queue_content(self):
        content = ''
        while not self.keyboard_queue.empty():
            content += self.keyboard_queue.get()
        content = content[:-1]
        return content

    def run(self):
        super().run()
        log.info(self.description)
        self.program()
        driver = UartDriver().connect()
        self.setup()
        log.info("Press the ENTER key to stop:\n")
        while self.keyboard_queue.empty():
            print('%s' % driver.read().decode('ascii').replace('\n', ''))
        self.thread_running = False
        self.input_thread.join()


log = logging.getLogger("{}.{}".format(TutorialBoardAdc.__module__, TutorialBoardAdc.__name__))
