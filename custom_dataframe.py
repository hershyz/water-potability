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