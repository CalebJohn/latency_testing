import json
import pandas as pd


df = pd.read_csv("delays.csv")


def calc_stats(delays):
    # remove outliers
    delays = delays.where(delays > 0.1).where(delays < 0.4).dropna()

    print("\nmean:  ", delays.mean())
    print("median:", delays.median())
    print("std. dev.:", delays.std())
    print("max:   ", delays.max())
    print("min:   ", delays.min())


calc_stats(df["Base"])
calc_stats(df["Kanata"])
calc_stats(df["keyd"])
