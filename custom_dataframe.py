# returns csv data in the form of a 2D array
def get_dataframe(csv_path):
    f = open(csv_path)
    point_arr = []
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        line = line.replace('\n', '')
        point_arr.append(line.split(','))
    return point_arr

# convert to floats
def convert_numerical(df_raw):
    curr_conversion = 0
    string_map = {}
    converted_df = []
    for point in df_raw:
        converted_point = []
        for feature in point:
            try:
                converted_point.append(float(feature))
            except:
                if feature not in string_map:
                    string_map[feature] = curr_conversion
                    curr_conversion += 1
                converted_point.append(string_map[feature])
        converted_df.append(converted_point)
    return converted_df