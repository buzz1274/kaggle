from abc import ABC, abstractmethod

from downloader.logger.logger import JSONLogger


class DataRetrieve(ABC):
    """
    Abstract Base Class for retrieving and saving data from a
    specified location.

    Attributes:
        logger (JSONLogger):
            A logger instance for structured logging. If no logger is provided,
            a default instance of `JSONLogger` is created.
    """

    """
    Initializes the `DataRetrieve` class with a logger instance.

    Args:
        logger (JSONLogger | None): An optional logger instance for
        structured logging. If not provided, a default instance of
        `JSONLogger` is created.
    """

    def __init__(self, *, logger: JSONLogger | None = None) -> None:
        if not logger:
            self.logger = JSONLogger()
        else:
            self.logger = logger

    """
    Downloads a file from the specified location and saves it
    to the given path.

    Args:
        location (str): The source location (e.g., URL or file path) from
            where the file should be retrieved.
        save_path (str): The directory path where the file
            will be saved locally.
        file_names (list[str]): A list of file names to be retrieved
            from the specified location.

    Returns:
        bool: Returns `True` if all files are successfully
            downloaded and saved, otherwise `False`.

    Raises:
        NotImplementedError: This method must be implemented in a subclass.
    """

    @abstractmethod
    def get(
        self,
        location: str,
        save_path: str,
        file_names: list[str],
    ) -> bool:
        pass
