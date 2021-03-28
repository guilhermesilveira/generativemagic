import pandas as pd


class ResultsFrequency:
    def frequency_analysis(self, elements):
        print("Value counts:")
        print(pd.value_counts(elements))
        print()
        print("Value counts normalized:")
        print(pd.value_counts(elements, normalize=True) * 100)
        print()
        unique_count = len(pd.unique(elements))
        print(f"Unique elements: {unique_count}")
        return pd.value_counts(elements).index
