import custom_dataframe
import math

# classification function
def knn_classify(point, df):

    distances = []
    
    for row in df:
        curr_distance = 0
        for i in range(0, len(point) - 1):
            curr_distance += abs(point[i] - row[i]) ** 2
        curr_distance = math.sqrt(curr_distance)
        distances.append([curr_distance, row[len(row) - 1]])
    distances = sorted(distances, key=lambda x : x[0])
    
    zero_count = 0
    one_count = 0
    for i in range(0, 3):
        if distances[i][1] == 0:
            zero_count += 1
        else:
            one_count += 1
    
    if zero_count > one_count:
        return 0
    else:
        return 1


# get dataframe with floats
df_raw = custom_dataframe.get_dataframe('data.csv')
df_raw.pop(0)
df = custom_dataframe.convert_numerical(df_raw)

# get actual outputs
actual = []
for point in df:
    actual.append(point[len(point) - 1])

# make predictions
predictions = []
for point in df:
    predictions.append(knn_classify(point, df))

# test accuracy:
correct = 0
for i in range(0, len(actual)):
    if actual[i] == predictions[i]:
        correct += 1
print('knn accuracy: ' + str(correct / len(actual)))