import pandas as pd


class CSVSerializer:
    def csv_serialize(self, filename, df):
        df.to_csv(filename)

    def csv_deserialize(self, filename):
        df = pd.read_csv(filename)

        return df
