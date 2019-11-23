import logging
import sys
import threading
from queue import Queue
from controller_board.uart_driver import UartDriver
from scenarios.scenario import Scenario


class TutorialBoardAdc(Scenario):
    name = 'Tutorial Board: ADC'

    def __init__(self):
        super().__init__()
        self.binary_file_name = 'tutorial_board_adc.bin'
        self.description = 'In this scenario, adc values on the potentiometer are read and shown, change the value on' \
                           'the potentiometer and make sure the values change'
        self.keyboard_queue = Queue()
        self.input_thread = None
        self.thread_running = False

    def add_input(self, input_queue):
        while self.thread_running:
            input_queue.put(sys.stdin.read(1))
        log.debug("this function is exiting now")

    def setup_keyboard_thread(self):
        self.input_thread = threading.Thread(target=self.add_input, args=(self.keyboard_queue,))
        self.thread_running = True
        self.input_thread.start()

    def setup(self):
        self.setup_keyboard_thread()

    def teardown_thread(self):
        self.thread_running = False
        log.debug("thread must exit now")
        self.input_thread.join()
        log.debug("thread joined")
        self.input_thread = None

    def get_keyboard_queue_content(self):
        content = ''
        while not self.keyboard_queue.empty():
            content += self.keyboard_queue.get()
        content = content[:-1]
        return content

    def output_on_new_line(self, msg):
        print('\r%s' % msg, end='\r')

    def run(self):
        super().run()
        log.info(self.description)
        self.program()
        self.driver = UartDriver().connect()
        self.setup()
        log.info("Press the ENTER key to stop:\n")
        while self.keyboard_queue.empty():
            message = self.driver.read().decode('ascii').replace('\n', '')
            print('%s' % message)

        log.debug("about to call teardown")
        self.teardown()

    def teardown(self):
        log.debug("called teardown")
        log.info("Press the ENTER key again")
        self.teardown_thread()
        self.driver.close()
        log.debug("driver closed")


log = logging.getLogger("{}.{}".format(TutorialBoardAdc.__module__, TutorialBoardAdc.__name__))
