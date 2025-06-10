import os

from kaggle import api

from downloader.data_retrieve.data_retrieve import DataRetrieve


class KaggleRetrieve(DataRetrieve):
    """
    A concrete implementation of the `DataRetrieve` abstract base class,
    specifically for retrieving data from Kaggle datasets.

    This class uses the Kaggle API to download and extract dataset files
    from a specified emote path and checks for the presence
    of the specified files in the target directory.

    Attributes:
        logger (JSONLogger):
            Inherited from the parent `DataRetrieve` class. Used to log
            actions and errors during the data retrieval process.
    """

    """
    Downloads and extracts a Kaggle dataset to the specified local directory.

    This method uses the Kaggle API to download a dataset located at
    `remote_path` and save it into the directory specified
    by `save_path`. The specified `file_names` are then checked
    to ensure they exist after extraction.

    Args:
        remote_path (str): The remote path on Kaggle where the dataset is
             located. E.g., "username/dataset-name".
        save_path (str): The local directory where the dataset files will be
                         downloaded and extracted.
        file_names (list[str]): A list of file names that should be present
                                in the downloaded dataset after extraction.

    Returns:
         bool: Returns `True` if all specified files are successfully found
               in the `save_path` directory after the download and
               extraction process.
               Returns `False` if any file is missing or an error occurs.

    Raises:
         Exception: If any critical error occurs during the downloading or
                    extraction process, it will be logged, and the method will
                    return `False` instead of raising the error.
    """

    def get(
        self,
        remote_path: str,
        save_path: str,
        file_names: list[str],
    ) -> bool:
        try:
            self.logger.info(f"Download of {remote_path} started.")
            api.dataset_download_files(remote_path, save_path, unzip=True)
            self.logger.info(
                f"Download and extraction of {remote_path} completed."
            )

            success: bool = True

            for file_name in file_names:

                if not os.path.exists(f"{save_path}/{file_name}"):
                    self.logger.error(f"{file_name} not found in {save_path}.")

                    success = False
                else:
                    self.logger.info(
                        f"{file_name} successfully downloaded "
                        f"and extracted to {save_path}."
                    )

            return success

        except Exception as e:
            self.logger.critical(
                f"An error occurred while downloading {remote_path}: {e}."
            )

            return False
