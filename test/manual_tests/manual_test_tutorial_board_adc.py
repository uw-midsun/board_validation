import logging
from ms_logging.ms_logger_configurator import MsLoggerConfigurator
from scenarios.tutorial_board_adc import TutorialBoardAdc


if __name__ == '__main__':
    MsLoggerConfigurator().configure_logging()
    log = logging.getLogger()
    TutorialBoardAdc().run()
