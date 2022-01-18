#!/usr/bin/env python3
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json

tiktok = AppStore(country="us", app_name="Lifetime Digital")

tiktok.review(how_many=5000)

df = pd.DataFrame(np.array(tiktok.reviews),columns=['review'])

df2 = df.join(pd.DataFrame(df.pop('review').tolist()))

df2.head()

df2.to_csv('C:/Users/flami/Downloads/SGF/LTH/App Store Reviews LifeTime Digital.csv') #Your Path you want to store it in
