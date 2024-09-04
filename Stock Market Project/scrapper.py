from util import *
import pandas as pd

url = 'https://www.5paisa.com/stocks/all'

stocks_list = stocks_url_getter(url)

for i in range(201, 3001, 100):
    df = get_stock_info(stocks_list[i]['link'])
    # print(df.empty)
    for stock in stocks_list[i+1:i+100]:
        temp = get_stock_info(stock['link'])
        if temp.empty == False:
            df = pd.concat([df, temp], axis=0, ignore_index=True)

    df.to_csv(f"M:/cei-internship/Stock Market Project/Stocks {i}-{i+99}.csv")