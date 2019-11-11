import logging
from ms_logging.ms_logger_configurator import MsLoggerConfigurator
from scenarios.blinking_led import BlinkingLed

if __name__ == '__main__':
    MsLoggerConfigurator().configure_logging()
    log = logging.getLogger()
    BlinkingLed().run()
