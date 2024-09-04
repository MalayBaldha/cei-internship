import pandas as pd

data = pd.read_csv("M:/cei-internship/Stock Market Project/Stocks 1-100.csv")

for i in range(101, 3001, 100):
    df = pd.read_csv(f"M:/cei-internship/Stock Market Project/Stocks {i}-{i+99}.csv")
    data = pd.concat([data, df], axis=0, ignore_index=True)

data.to_csv("M:/cei-internship/Stock Market Project/Stocks Data 1-3000.csv")