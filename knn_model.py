import custom_dataframe

# regression function
def xy_regression(points):
    xy_data = []
    x = []
    y = []
    xy = []
    x2 = []

    x_sum = 0
    y_sum = 0
    xy_sum = 0
    x2_sum = 0

    for point in points:
        xy_data.append(point)

    for point in xy_data:
        xy.append(point[0] * point[1])
        x2.append(point[0] * point[0])
        x.append(point[0])
        y.append(point[1])

    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(xy)
    x2_sum = sum(x2)

    a = (y_sum * x2_sum) - (x_sum * xy_sum)
    a /= (len(xy_data) * x2_sum) - (x_sum * x_sum)

    b = (len(xy_data) * xy_sum) - (x_sum * y_sum)
    b /= (len(xy_data) * x2_sum) - (x_sum * x_sum)

    return [a, b] # a = intercept, b = coefficient


# predict with linear
def linear_prediction(x, model):
    return (x * model[1]) + model[0]


# get dataframe with floats
df_raw = custom_dataframe.get_dataframe('data.csv')
df_raw.pop(0)
df = custom_dataframe.convert_numerical(df_raw)

# get linear models for each input feature
linear_models = []
for i in range(0, len(df[0]) - 1):
    points = [] # x = input feature, y = output
    for row in df:
        points.append([row[i], row[len(row) - 1]])
    linear_models.append(xy_regression(points))

# get actual outputs
actual = []
for point in df:
    actual.append(point[len(point) - 1])

# make predictions
predictions = []
for point in df:
    curr_prediction = 0
    for i in range(0, len(point) - 1):
        curr_prediction += linear_prediction(point[i], linear_models[i])
    curr_prediction /= (len(point) - 1)
    if abs(0 - curr_prediction) < abs(1 - curr_prediction):
        predictions.append(0)
    else:
        predictions.append(1)

# test accuracy:
correct = 0
for i in range(0, len(actual)):
    if actual[i] == predictions[i]:
        correct += 1
print('linear regression accuracy: ' + str(correct / len(actual)))