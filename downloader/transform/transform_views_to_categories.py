import json

import pandas as pd

from downloader.data_output.data_output import DataOutput
from downloader.transform.transform import Transform


class TransformViewsToCategories(Transform):
    """

    This class is responsible for transforming video view data into
    category-based aggregated views. The transformation process merges
    video and category information, computes total views per category, and
    prepares the data for output generation.

    Attributes:
        dataframe (pd.DataFrame | None):
            Inherited from the `Transform` base class. Stores the resulting
            transformed DataFrame after the transformation process.

        logger (JSONLogger):
            Inherited from the `Transform` base class. Used to log information,
            warnings, and errors during the transformation process.
    """

    """
    Transforms video view data into aggregated category-level view data.

    This method performs the following steps:
    - Reads video data and category data from CSV and JSON files.
    - Aggregates video views per category.
    - Merges video views data with corresponding category details.
    - Normalizes the number of views by dividing them by 1,000,000.
    - Sorts the data by the number of views in descending order and removes
      any rows with missing category information.
    - Stores the transformed data into `self.dataframe`.
    - Generates outputs using the provided `data_outputs`.

    Args:
        paths (dict[str, str]):
            A dictionary containing file paths used during the transformation.
            The dictionary must include:
            - `"video_file_path"`: The path to the CSV file containing video
              data with "category_id" and "views" columns.
            - `"category_file_path"`: The path to the JSON file containing
              category information with "id" and "snippet.title".
            - `"output_path"`: The directory where output files will be saved.
        data_outputs (list[DataOutput]):
            A list of `DataOutput` instances to define and handle
            the output generation process for the transformed data.

    Returns:
        None
    """

    def transform(
        self,
        paths: dict[str, str],
        data_outputs: list[DataOutput],
    ) -> None:
        self.logger.info("Starting TransformViewsToCategories")

        videos_dataframe = self.csv_to_dataframe(paths["video_file_path"])[
            ["category_id", "views"]
        ]

        categories_dataframe = self._json_to_dataframe(
            paths["category_file_path"]
        )[["id", "snippet.title"]]

        categories_dataframe["id"] = categories_dataframe["id"].astype(int)

        videos_dataframe = (
            videos_dataframe.groupby("category_id")["views"]
            .sum()
            .reset_index()
        )

        videos_dataframe = videos_dataframe.merge(
            categories_dataframe,
            left_on="category_id",
            right_on="id",
            how="left",
        )

        videos_dataframe = videos_dataframe.sort_values(
            by=["views"], ascending=[False]
        ).dropna()

        videos_dataframe["views"] = videos_dataframe["views"] / 1_000_000

        self.dataframe = videos_dataframe

        self.logger.info("Completed TransformViewsToCategories")

        for output in data_outputs:
            output.generate(self.dataframe, paths["output_path"])

    """
    converts the categories json file into a pandas dataframe
    """

    def _json_to_dataframe(self, file_path: str) -> pd.DataFrame:
        with open(file_path) as f:
            json_data = json.load(f)

        return pd.json_normalize(json_data["items"])
