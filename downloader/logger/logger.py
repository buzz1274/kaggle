import logging
from typing import Any, Optional

from pythonjsonlogger import jsonlogger


class JSONLogger:
    """
    A utility class for creating JSON-structured logs.

    The `JSONLogger` provides logging with JSON formatting using the
    `python-json-logger`

    Attributes:
        logger (logging.Logger):
            The underlying logger instance used to handle the logging logic.
    """

    """
    Initializes a JSONLogger instance with a specified logfile and log level.

    Args:
        file_name (Optional[str]):
            The name of the file where log messages will be stored.
            Defaults to "app_log.json".
        level (Optional[int]):
            The logging level to be set for the logger.
            Defaults to `logging.INFO`.
    """

    def __init__(
        self,
        file_name: Optional[str] = "app_log.json",
        level: Optional[int] = logging.INFO,
    ):
        self.logger = logging.getLogger("JSONLogger")
        self.logger.setLevel(level)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(file_name)
            file_handler.setFormatter(self._get_json_formatter())
            self.logger.addHandler(file_handler)

    """
    Creates and configures a JSON formatter for the logger.

    Returns:
        logging.Formatter:
            An instance of the JSON formatter used to structure log messages.
    """

    def _get_json_formatter(self) -> logging.Formatter:
        return jsonlogger.JsonFormatter(  # type: ignore[attr-defined]
            "%(asctime)s %(levelname)s %(name)s %(message)s %(module)s "
            "%(funcName)s %(lineno)d %(extra)s",
        )

    """
    Logs a message with the specified level and additional context.

    Args:
        level (int): The log level (e.g., `logging.INFO`, `logging.ERROR`).
        message (str): The main log message to record.
        **kwargs (Any): Additional details to include in the log entry as
                        part of the `extra` field.

    Returns:
        None
    """

    def log(self, level: int, message: str, **kwargs: Any) -> None:
        self.logger.log(level, message, extra={"extra": kwargs}, stacklevel=3)

    def info(self, message: str, **kwargs: Any) -> None:
        """Log a message with the INFO level."""
        self.log(logging.INFO, message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        """Log a message with the DEBUG level."""
        self.log(logging.DEBUG, message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        """Log a message with the WARNING level."""
        self.log(logging.WARNING, message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        """Log a message with the ERROR level."""
        self.log(logging.ERROR, message, **kwargs)

    def critical(self, message: str, **kwargs: Any) -> None:
        """Log a message with the CRITICAL level."""
        self.log(logging.CRITICAL, message, **kwargs)
