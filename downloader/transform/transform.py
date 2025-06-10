from abc import ABC, abstractmethod

import pandas as pd

from downloader.data_output.data_output import DataOutput
from downloader.logger.logger import JSONLogger


class Transform(ABC):
    """
    Abstract Base Class for defining data transformation pipelines.

    This class provides a flexible and extensible framework for implementing
    custom data transformations. Subclasses must implement the
    `transform` method, which specifies the logic for processing
    input files and producing outputs.

    Attributes:
        dataframe (pd.DataFrame | None):
            Stores a pandas DataFrame for manipulating and processing data.
             The dataframe` property provides a getter and
             setter for this attribute.

        logger (JSONLogger):
            A structured logger instance used to log events, errors, or
            debugging information during the transformation process.
    """

    @property
    def dataframe(self) -> pd.DataFrame | None:
        return self._dataframe

    @dataframe.setter
    def dataframe(self, value: pd.DataFrame | None) -> None:
        self._dataframe = value

    """
    Initializes the `Transform` class with an optional logger instance.

    Args:
        logger (JSONLogger | None): A logger instance for structured
        logging. If not provided, a new instance of `JSONLogger` is created.
    """

    def __init__(self, *, logger: JSONLogger | None = None) -> None:
        self.dataframe: pd.DataFrame | None = None

        if not logger:
            self.logger = JSONLogger()
        else:
            self.logger = logger

    """
    Abstract method for performing a data transformation.

    Args:
        paths (dict[str, str]): A dictionary mapping logical names to file
        paths used during the transformation process. For example, paths may
        specify the location of input or output files.

        output (list[DataOutput]): A list of `DataOutput` instances defining
        the outputs to be generated during transformation.

    Returns:
        None

    Raises:
        NotImplementedError: If the method is not implemented in a subclass.
    """

    @abstractmethod
    def transform(
        self, paths: dict[str, str], output: list[DataOutput]
    ) -> None:
        pass

    """
    Load a CSV file into a pandas DataFrame.

    This function reads the contents of a CSV file from the
    specified `filepath` and converts it into a pandas DataFrame for
    further data manipulation or analysis.

    Args:
        file_path (str): The file_path from
            where the file should be retrieved.

    Returns:
        pd.DataFrame
    """

    def csv_to_dataframe(self, file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)
