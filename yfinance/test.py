#!/usr/bin/env python3
# build a giant stocks DF, write them to data file for analysis for later on

# $ pip3 install -e . : install the dev version
# $ python3 -m yfinance.ticker : run ticker.py (workaround for its relative path include)

import yfinance as yf
import os

symbols = list(sp500df['Symbol'])
res_dict = {}
dest_dir = '~/projects/yfinance/data/'
for s in symbols:
    t = yf.Ticker(s)
    res_dict[s] = t.info

info_df = pd.DataFrame.from_dict(res_dict)
info_df.to_csv(os.path.join(dest_dir, 'sp500_info.csv'))