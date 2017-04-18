import pandas as pd
url = "http://stat.columbia.edu/~rachel/datasets/nyt1.csv"
data1 = pd.read_csv(url)

# 1. Create a new variable, age_group, that categorizes users as "<18",
#    "18-24", "25-34", "35-44", "45-54", "55-64", and "65+".
def get_age_group(column):
    if column < 18:
        return "<18"
    elif column <= 24:
        return "18-24"
    elif column <= 34:
        return "25-34"
    elif column <= 44:
        return "35-44"
    elif column <= 54:
        return "45-54"
    elif column <= 64:
        return "55-64"
    else:
        return "65+"

data1['age_group'] = data1["Age"].apply(get_age_group)
