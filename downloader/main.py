import argparse
import os

from downloader.data_output.output_views_to_categories import (
    ViewsToCategoriesBarChart,
    ViewsToCategoriesJSON,
)
from downloader.data_retrieve.kaggle_retrieve import KaggleRetrieve
from downloader.logger.logger import JSONLogger
from downloader.transform.transform_views_to_categories import (
    TransformViewsToCategories,
)

OWNER_SLUG = "datasnaek"
DATASET_SLUG = "youtube-new"
DATASET_VERSION = "115"

parser = argparse.ArgumentParser("kaggle_importer")
parser.add_argument(
    "owner_slug",
    help=f"Owner slug for dataset(default={OWNER_SLUG}).",
    nargs="?",
    default=OWNER_SLUG,
    type=str,
)
parser.add_argument(
    "dataset_slug",
    help=f"Slug for dataset(default={DATASET_SLUG}).",
    nargs="?",
    default=DATASET_SLUG,
    type=str,
)
parser.add_argument(
    "dataset_version",
    help=f"Dataset version(default={DATASET_VERSION}).",
    nargs="?",
    default=DATASET_VERSION,
    type=str,
)

args = parser.parse_args()

location = f"{args.owner_slug}/{args.dataset_slug}"
save_path = (
    f"/{os.environ['TMP_SAVE_DIRECTORY']}/kaggle/"
    f"{args.owner_slug}/{args.dataset_slug}/{args.dataset_version}/"
)
output_save_path = (
    f"./downloader/visualisations/kaggle/{args.owner_slug}/"
    f"{args.dataset_slug}/{args.dataset_version}/"
)
log_path = "./downloader/logs/"

if not os.path.exists(output_save_path):
    os.makedirs(os.path.dirname(output_save_path))

if not os.path.exists(log_path):
    os.makedirs(os.path.dirname(log_path))

logger = JSONLogger(
    file_name=f"{log_path}/project_logs.json",
)

logger.info("Kaggle retrieve and transform started")

if KaggleRetrieve(logger=logger).get(
    location,
    save_path,
    ["GBvideos.csv", "GB_category_id.json"],
):
    TransformViewsToCategories().transform(
        {
            "video_file_path": f"{save_path}/GBvideos.csv",
            "category_file_path": f"{save_path}/GB_category_id.json",
            "output_path": f"{output_save_path}",
        },
        [
            ViewsToCategoriesBarChart(logger=logger),
            ViewsToCategoriesJSON(logger=logger),
        ],
    )

logger.info("Kaggle retrieve and transform completed")
