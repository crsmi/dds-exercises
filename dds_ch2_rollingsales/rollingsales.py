import pandas as pd
boroughs = ["bronx","brooklyn","manhattan","queens","statenisland"]
frames = []
for borough in boroughs:
    frames.append(pd.read_excel("rollingsales_" + borough + ".xls",skiprows=4))
data = pd.concat(frames)
