import pandas as pd
import custom_dataframe
import matplotlib.pyplot as plt

# get dataframe(s)
pandas_df = pd.read_csv(r'data.csv')
df = custom_dataframe.get_dataframe('data.csv')

# get input/output parameters
feature_line = df[0]
output = feature_line[len(feature_line) - 1]
features = []
for i in range(0, len(feature_line) - 1):
    features.append(feature_line[i])

# scatter plots
for feature in features:
    pandas_df.plot(kind='scatter', x=feature, y=output)
    plt.show()

# box plots
for feature in features:
    pandas_df[feature].plot(kind='box')
    plt.show()