import pandas as pd
import pytest


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [4, 5, 6],
        }
    )
