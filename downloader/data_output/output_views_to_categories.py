import matplotlib.pyplot as plt
import pandas as pd

from downloader.data_output.data_output import DataOutput


class ViewsToCategoriesBarChart(DataOutput):
    """
    Generates and saves a bar chart that visualizes YouTube views
    per category.

    This implementation creates a bar chart using the provided dataset and
    saves it to the specified location.

    Methods:
        generate(data: pd.DataFrame, save_path: str | None):
            Generates and saves a bar chart using the provided dataset.
    """

    """
    Generates and saves a bar chart showing YouTube views by category.

    Args:
        data (pd.DataFrame): The dataset containing "snippet.title" and
                             "views" columns.
        save_path (str | None): The directory path where the chart image
                                should be saved.

    Returns:
        None

    Raises:
        ValueError: Logs an error if the provided dataset is empty.
    """

    def generate(self, data: pd.DataFrame, save_path: str | None) -> None:
        self.logger.info("Starting Output ViewsToCategories as Bar Chart")

        if data.empty:
            self.logger.error(
                "Output ViewsToCategories as Bar Chart failed empty data"
            )

        plt.bar(
            data["snippet.title"],
            data["views"],
            color="skyblue",
        )

        plt.xlabel("Category")
        plt.ylabel("Views(millions)")
        plt.tick_params(axis="x", labelrotation=90)
        plt.title("Youtube Views by Category")
        plt.savefig(f"{save_path}/views_to_categories_bar_chart.png")

        self.logger.info("Complete Output ViewsToCategories as Bar Chart")


class ViewsToCategoriesJSON(DataOutput):
    """
    Generates and saves a json file that contains YouTube views
    per category.

    This implementation converts the provided dataset into a JSON file
    and saves it to the specified location.

    Methods:
        generate(data: pd.DataFrame, save_path: str):
            Converts the provided dataset into a JSON file and saves it.
    """

    """
    Generates and saves a json file containing YouTube views by category.

    Args:
        data (pd.DataFrame): The dataset containing "snippet.title" and
                             "views" columns.
        save_path (str | None): The directory path where the chart image
                                should be saved.

    Returns:
        None

    Raises:
        ValueError: Logs an error if the provided dataset is empty.
    """

    def generate(self, data: pd.DataFrame, save_path: str) -> None:
        self.logger.info("Starting Output ViewsToCategories as JSON")

        if data.empty:
            self.logger.error(
                "Output ViewsToCategories as JSON failed empty data"
            )

        data.to_json(f"{save_path}/views_to_categories.json", orient="records")

        self.logger.info("Complete Output ViewsToCategories as JSON")
