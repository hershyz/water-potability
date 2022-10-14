import custom_dataframe
from copy import deepcopy

# get dataframe with floats
df_raw = custom_dataframe.get_dataframe('data.csv')
cats = df_raw[0]
df_raw.pop(0)
df = custom_dataframe.convert_numerical(df_raw)

# get mean map
def mean_map(df):
    
    # initialize the map
    n_features = len(df[0]) - 1
    cat_freqs = {}

    for i in range(0, len(df)):
        curr_cat = df[i][len(df[0]) - 1]
        if curr_cat in cat_freqs:
            cat_freqs[curr_cat] += 1
        if curr_cat not in cat_freqs:
            cat_freqs[curr_cat] = 0

    init_arr = []
    for i in range(0, n_features):
        init_arr.append(0)
    
    map = {}
    for cat in cat_freqs:
        map[cat] = init_arr
    

    # sum values in the map
    for point in df:
        curr_cat = point[len(point) - 1]
        arr = deepcopy(map[curr_cat])
        for i in range(0, len(point) - 1):
            arr[i] += float(point[i])
        map[curr_cat] = arr
    

    # divide by frequencies of unique categories to find averages
    for cat in map:
        arr = deepcopy(map[cat])
        for i in range(0, len(arr)):
            arr[i] /= cat_freqs[cat]
        map[cat] = arr
    
    return map

mean_map = mean_map(df)

# get stddev map
stddev_map = {}
freqs = {}
freqs[0] = 0
freqs[1] = 0
stddev_map[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
stddev_map[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for point in df:
    output = int(point[len(point) - 1])
    freqs[output] = freqs[output] + 1
    mean_arr = mean_map[output]
    curr_arr = deepcopy(stddev_map[output])
    for i in range(0, len(point) - 1):
        dist = abs(point[i] - mean_arr[i])
        curr_arr[i] += dist
    stddev_map[output] = curr_arr

for cat in stddev_map:
    curr_arr = deepcopy(stddev_map[cat])
    for i in range(0, len(curr_arr)):
        curr_arr[i] /= freqs[cat]
    stddev_map[cat] = curr_arr

print('not potable stats:')
mean_arr_0 = mean_map[0]
stddev_arr_0 = stddev_map[0]
for i in range(0, len(mean_arr_0)):
    print(cats[i] + ' - mean: ' + str(mean_arr_0[i]) + ', std dev: ' + str(stddev_arr_0[i]))

print('---')
print('potable stats:')
mean_arr_1 = mean_map[1]
stddev_arr_1 = stddev_map[1]
for i in range(0, len(mean_arr_1)):
    print(cats[i] + ' - mean: ' + str(mean_arr_1[i]) + ', std dev: ' + str(stddev_arr_1[i]))