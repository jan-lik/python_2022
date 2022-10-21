import pandas as pd
import numpy as np
f = pd.read_csv("video-games.csv")
#1
n_games = len(f['title'].value_counts())
print(n_games)
#2
by_years = f.groupby(["year"]).agg({"title":"count"})
print(by_years)
#3
mean_price = f.groupby(["publisher"]).agg({"price":"mean"})
print(mean_price)
#4
age_max_price = f.groupby(["age_raiting"]).agg({"price":"max"})
print(age_max_price)
#6
min_max_price = f.groupby(["age_raiting"]).agg({"price":"max"})
min_max_price['min_price'] = f.groupby(["age_raiting"]).agg({"price":"min"})
min_max_price['sales_metric'] = f.groupby(["age_raiting"]).agg({"sales_metric":"min"})
print(min_max_price)

n_games_by_age = f.groupby(["review_rating"]).agg({"title":"count"})
print(n_games_by_age)

max_raiting_by_years = f.groupby(["year"]).agg({"review_rating":"count"})
print(max_raiting_by_years)