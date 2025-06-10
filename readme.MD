<u>To install</u>

1. Clone this repo `git clone https://github.com/buzz1274/kaggle`
2. Rename compose.env.example to compose.env
3. Fill in appropriate values in compose.env
4. From the root folder execute `./manage.sh install`

<u>Execution of Importer</u>:

1. For help execute `./manage.sh generate -h`
2. Executing `./manage.sh generate` will generate a graph using the default arguments
3. The graph output will be saved to  `downloader/visualisations/kaggle/datasnaek/youtube-new/115`
   it can then be viewed by running `open ./downloader/visualisations/kaggle/datasnaek/youtube-new/115/bar_chart.png`
4. Example logs can be viewed at `./example_logs.json`

<u>Helper commands</u>:

1.  `./manage.sh tests` will execute all unit tests.
2.  `./manage.sh mypy` will check code for correct types.
3.  `./manage.sh logs` will follow docker-compose logs.


<u>ADRs</u>

1. Logging: Use JsonFormatter from python-json-logger for structured JSON logging.
2. Download: Integrated Kaggle API for dataset downloads.
3. Data Manipulation: Use pandas for efficient data processing, cleaning, and analysis workflows.
4. Data Visualization: Use matplotlib to create customizable visualizations for insights derived from the data.
5. Type Hints: Add Python type hints for better readability and static analysis using mypy.
6. Dependencies: Manage dependencies using poetry.
7. Error Handling: Centralized exception handling for fault tolerance and easier debugging.
8. Testing: Use pytest with unit tests for all major modules to ensure reliability.
9. Version Control: Git with feature branches.
10. Containerization: Use Docker for consistent development and production environments.
11. Documentation: Maintain README.md and docstrings for project and module documentation.
12. Pre-commit Hooks: Use pre-commit for automated code linting and formatting. Tools included:
    Black: Python code formatter.
    Flake8: Linter to ensure PEP8 compliance.
    isort: Organizes imports automatically.
    Bandit: Discover security issues.
