import logging
from ms_logging.log_colors import LogColors


class MsLoggerConfigurator(object):
    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ = "\033[1m"
    COLORS = {
        'WARNING': LogColors.YELLOW,
        'INFO': LogColors.GREEN,
        'DEBUG': LogColors.WHITE,
        'CRITICAL': LogColors.WHITE_RED_BG,
        'ERROR': LogColors.RED
    }

    class ColoredFormatter(logging.Formatter):
        def __init__(self, msg):
            logging.Formatter.__init__(self, msg)

        def format(self, record):
            level_name = record.levelname
            record.levelname = self.colorize(level_name, level_name)
            # record.msg = self.colorize(record.msg, level_name) # uncomment if want msg to be colorized as well
            return logging.Formatter.format(self, record)

        def colorize(self, text, levelname):
            return MsLoggerConfigurator.COLOR_SEQ % MsLoggerConfigurator.COLORS[levelname].value \
                   + text + MsLoggerConfigurator.RESET_SEQ

    def formatter_message(self, message):
        return message.replace("$RESET", MsLoggerConfigurator.RESET_SEQ)\
            .replace("$BOLD", MsLoggerConfigurator.BOLD_SEQ)

    def configure_logging(self, log_level=logging.DEBUG):
        #FORMAT = "[%(levelname)-18s] $BOLD%(filename)-s$RESET:%(lineno)-d %(message)s "
        FORMAT = "[%(levelname)s] %(message)s "
        COLOR_FORMAT = self.formatter_message(FORMAT)
        color_formatter = MsLoggerConfigurator.ColoredFormatter(COLOR_FORMAT)
        console = logging.StreamHandler()
        console.setLevel(log_level)
        console.setFormatter(color_formatter)
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(console)
