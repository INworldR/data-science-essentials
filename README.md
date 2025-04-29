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

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- scikit-learn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-science-essentials.git
cd data-science-essentials
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Example usage of the DataCleaner class:

```python
from lib.core_classes import DataCleaner

# Initialize and load data
cleaner = DataCleaner()
cleaner.load_data("data/raw/your_data.csv")

# Apply cleaning operations
cleaner.remove_duplicates()\
       .handle_missing_values(strategy='mean')\
       .encode_categorical(['category_column'])\
       .scale_features(['numeric_column'])

# Get cleaned data
clean_df = cleaner.get_clean_data()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms included in the LICENSE file.
