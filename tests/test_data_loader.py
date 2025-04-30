import pytest
import pandas as pd
from pathlib import Path
from lib.core_classes import DataLoader

def test_data_loader_initialization():
    """Test basic initialization of DataLoader."""
    loader = DataLoader(use_mock=True)
    assert loader.df is not None
    assert isinstance(loader.df, pd.DataFrame)
    assert not loader.cache_locally
    assert len(loader.df) == 10  # Mock data has 10 rows

def test_data_loader_with_caching():
    """Test DataLoader with caching enabled."""
    # Ensure clean state
    cache_path = Path("data/raw/titanic.csv")
    if cache_path.exists():
        cache_path.unlink()
    
    # Test with caching
    loader = DataLoader(cache_locally=True, use_mock=True)
    assert loader.cache_locally
    
    # Verify DataFrame
    assert len(loader.df) == 10
    assert 'PassengerId' in loader.df.columns
    assert 'Survived' in loader.df.columns

def test_data_loader_with_local_file(tmp_path):
    """Test DataLoader with a local CSV file."""
    # Create a test CSV file
    test_data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    test_file = tmp_path / "test.csv"
    test_data.to_csv(test_file, index=False)
    
    # Test loading local file
    loader = DataLoader(filepath=str(test_file))
    assert len(loader.df) == 3
    assert list(loader.df.columns) == ['A', 'B']

def test_data_loader_error_handling():
    """Test error handling in DataLoader."""
    # Test with non-existent file
    with pytest.raises(FileNotFoundError):
        DataLoader(filepath="non_existent.csv")

def test_mock_data_structure():
    """Test the structure of mock data."""
    loader = DataLoader(use_mock=True)
    df = loader.df
    
    # Check columns
    expected_columns = [
        'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
        'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
    ]
    assert all(col in df.columns for col in expected_columns)
    
    # Check data types
    assert df['PassengerId'].dtype in ['int32', 'int64']
    assert df['Survived'].dtype in ['int32', 'int64']
    assert df['Sex'].dtype == 'object'
    assert df['Age'].dtype in ['float64', 'int64'] 