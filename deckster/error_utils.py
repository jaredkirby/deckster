# error_utils.py

import logging


def setup_logging(log_file: str, log_level: int = logging.DEBUG) -> None:
    """
    Sets up logging configuration.

    Args:
        log_file: The path to the log file.
        log_level: The logging level (default is logging.DEBUG).
    """
    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def log_error(error_message: str) -> None:
    """
    Logs an error message.

    Args:
        error_message: The error message to be logged.
    """
    logging.error(error_message)


def log_exception(exception: Exception) -> None:
    """
    Logs an exception with its traceback.

    Args:
        exception: The exception to be logged.
    """
    logging.exception(f"An exception occurred: {exception}")


class PowerPointError(Exception):
    """
    Custom exception class for PowerPoint-related errors.
    """

    pass
