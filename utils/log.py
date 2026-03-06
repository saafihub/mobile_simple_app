import os
import sys
from loguru import logger
import inspect

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
exec_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(exec_dir, "log")
os.makedirs(report_dir, exist_ok=True)


class LogConfig:

    def __init__(self, level: str = 'DEBUG', color_log: bool = True):
        self.logger = logger
        self._color_log = color_log
        self._console_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | {file} | {message}"
        )
        self._log_format = (
            "{time:YYYY-MM-DD HH:mm:ss} | "
            "<level>{level: <8}</level> | {file: <10} | {message}"
        )
        self._level = level
        self.logfile = os.path.join(report_dir, "test_log.log")
        self.set_level(self._color_log, self._console_format, self._level)

    def set_level(self, color_log: bool = True, log_format: str = None, level: str = "DEBUG"):
        if log_format is None:
            log_format = self._console_format

        self.logger.remove()
        self._level = level

        self.logger.add(
            sys.stderr,
            level=level,
            colorize=color_log,
            format=log_format
        )
        self.logger.add(
            self.logfile,
            level=level,
            colorize=False,
            format=self._log_format,
            encoding="utf-8"
        )


log_cfg = LogConfig(level="TRACE")
log = logger