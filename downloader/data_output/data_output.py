from abc import ABC, abstractmethod

import pandas as pd

from downloader.logger.logger import JSONLogger


class DataOutput(ABC):
    """
    Abstract Base Class for generating and saving data output.

    This class defines a common interface for creating data outputs in various
    formats.

    Attributes:
        logger (JSONLogger):
            A logger instance for structured logging. If no logger is provided,
            a default instance of `JSONLogger` is created.
    """

    def __init__(self, *, logger: JSONLogger | None = None) -> None:
        if not logger:
            self.logger = JSONLogger()
        else:
            self.logger = logger

    """
    Abstract method to generate and save the output.

    Subclasses must provide an implementation for this method. The
    implementation should handle the processing and saving of the given
    data to the specified path.

    Args:
        data (pd.DataFrame): The dataset to be processed and saved.
        save_path (str): The file path where the generated output should be
                         saved.

    Returns:
        None

    Raises:
        NotImplementedError: If the method is not implemented by a subclass.
    """

    @abstractmethod
    def generate(
        self,
        data: pd.DataFrame,
        save_path: str,
    ) -> None:
        pass
