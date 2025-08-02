import pandas as pd
import unittest

from ..src.transformers.cleaner import clean


class TestClean(unittest.TestCase):


    def test_clean(self):
        # Arrange: create a DataFrame with dirty data
        df = pd.DataFrame({
            "title": [" Hello ", "   ", "World"],
            "journal": ["Science", None, " Nature "],
            "date": ["01/01/2020", "  ", "5 May 2021"]
        })

        # Act
        result = clean(df)

        # Assert

        # 1. Row with empty/space-only title should be removed
        self.assertEqual(len(result), 2)
        self.assertNotIn("   ", result["title"].values)

        # 2. All date values should be parsed into datetime-like objects
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result["date"]))

        # 3. No NaN values in 'title' column
        self.assertFalse(result["title"].isna().any())