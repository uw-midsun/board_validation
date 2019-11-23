import logging
from ms_logging.ms_logger_configurator import MsLoggerConfigurator
from scenarios.blinking_led import BlinkingLed
from scenarios.tutorial_board_adc import TutorialBoardAdc
from scenarios.tutorial_board_button_interrupt import TutorialBoardButtonInterrupt


def main():
    scenarios = [
        BlinkingLed,
        TutorialBoardAdc,
        TutorialBoardButtonInterrupt
    ]
    while True:
        log.info("Available scenarios: please input the number of the scenario that you would like to run. Type "
                 "\"exit\" to stop.")
        for i, s in enumerate(scenarios):
            log.info("[%d]: %s" % (i, s.name))
        choice = input()
        if choice == 'exit':
            break
        try:
            d = int(choice)
            if d >= len(scenarios):
                log.error("Invalid input, please try again")
                continue
        except Exception:
            log.error("Invalid input, please try again")
            continue
        scenario = scenarios[d]()
        scenario.run()


if __name__ == '__main__':
    MsLoggerConfigurator().configure_logging(log_level=logging.INFO)
    log = logging.getLogger()
    main()
