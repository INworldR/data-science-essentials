"""
Configuration settings for the Data Science Essentials project.
"""

import os
from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).parent.parent

# Data directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = DATA_DIR / "models"

# Source directories
SRC_DIR = ROOT_DIR / "src"
DATA_SRC_DIR = SRC_DIR / "data"
FEATURES_SRC_DIR = SRC_DIR / "features"
MODELS_SRC_DIR = SRC_DIR / "models"
VISUALIZATION_SRC_DIR = SRC_DIR / "visualization"

# Other directories
DOCS_DIR = ROOT_DIR / "docs"
TESTS_DIR = ROOT_DIR / "tests"
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"

# Create directories if they don't exist
for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    SRC_DIR,
    DATA_SRC_DIR,
    FEATURES_SRC_DIR,
    MODELS_SRC_DIR,
    VISUALIZATION_SRC_DIR,
    DOCS_DIR,
    TESTS_DIR,
    NOTEBOOKS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# Data file paths
TITANIC_RAW_DATA = RAW_DATA_DIR / "titanic.csv"
TITANIC_PROCESSED_DATA = PROCESSED_DATA_DIR / "titanic_processed.csv"

# Model file paths
TITANIC_MODEL = MODELS_DIR / "titanic_model.pkl"

# Logging configuration
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "data_science.log"

# Logging format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"

# Data processing configuration
RANDOM_SEED = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2

# Model configuration
MODEL_PARAMS = {
    "random_forest": {
        "n_estimators": 100,
        "max_depth": None,
        "random_state": RANDOM_SEED,
    },
    "logistic_regression": {
        "max_iter": 1000,
        "random_state": RANDOM_SEED,
    },
}

# Feature configuration
CATEGORICAL_FEATURES = ["Sex", "Embarked", "Pclass"]
NUMERICAL_FEATURES = ["Age", "Fare", "SibSp", "Parch"]
TARGET_FEATURE = "Survived"

# Visualization configuration
PLOT_STYLE = "seaborn"
FIGURE_SIZE = (10, 6)
DPI = 300

# Dataset configuration
USE_MOCK_DATA = True
DATASET_PATH = str(RAW_DATA_DIR)
PROCESSED_PATH = str(PROCESSED_DATA_DIR)

# Kaggle configuration (if needed)
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME", "")
KAGGLE_KEY = os.getenv("KAGGLE_KEY", "")

# Database configuration (if needed)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Model configuration
RANDOM_SEED = int(os.getenv("RANDOM_SEED", "42"))
TEST_SIZE = float(os.getenv("TEST_SIZE", "0.2"))
VALIDATION_SIZE = float(os.getenv("VALIDATION_SIZE", "0.2")) 