# Data Science Essentials

A comprehensive toolkit for data scientists providing essential utilities and workflows for data analysis and machine learning projects.

## Project Structure

```
data-science-essentials/
├── data/
│   ├── raw/          # Original, immutable data
│   └── processed/    # Cleaned and processed data
├── docs/             # Documentation files
├── lib/              # Core library functions and classes
├── report/           # Generated analysis and reports
├── src/             # Source code for use in this project
└── tests/           # Unit tests
```

## Features

- Data cleaning and preprocessing utilities
- Standardized data processing pipeline
- Categorical data encoding
- Feature scaling
- Missing value handling
- Duplicate removal
- SQL-like operations with DuckDB (optional)
- Automatic Titanic dataset loading from Kaggle

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- scikit-learn
- kaggle (optional, for downloading datasets)
- duckdb (optional, for SQL operations)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-science-essentials.git
cd data-science-essentials
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Kaggle Setup (Optional)

To use the Kaggle dataset functionality:

1. Create a Kaggle account at https://www.kaggle.com
2. Go to "Account" → "Create API Token"
3. Download `kaggle.json` and place it in `~/.kaggle/`
4. Set appropriate permissions:
```bash
chmod 600 ~/.kaggle/kaggle.json
```

## Usage

### Loading Data

```python
from lib.core_classes import DataLoader, DataCleaner

# Load Titanic dataset (requires Kaggle setup)
loader = DataLoader()

# Or use mock data for testing
loader = DataLoader(use_mock=True)

# Or load local CSV file
loader = DataLoader(filepath="data/raw/your_data.csv")

# Get the data
df = loader.df
```

### Data Cleaning

```python
# Initialize cleaner with data
cleaner = DataCleaner(df)

# Apply cleaning operations
clean_df = cleaner.remove_duplicates()\
                 .handle_missing_values(strategy='mean')\
                 .encode_categorical(['category_column'])\
                 .scale_features(['numeric_column'])\
                 .get_clean_data()
```

### SQL Operations (with DuckDB)

```python
# Execute SQL queries on DataFrame
result = cleaner.execute_sql("SELECT * FROM df WHERE column > 100")
```

## Testing

Run the tests with:

```bash
python -m pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms included in the LICENSE file.
