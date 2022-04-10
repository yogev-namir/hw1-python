import pandas

def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient=”list”)

def filter_by_feature(data, feature, values):
    data1={}
    data2={}
    for key in data.keys():
        data1.update(key)
        data2.update(key)
    for index,val in enumerate(data[feature]):
        if val in values:
            for key1 in data1.keys():
                data1[key1][index]=data[key1][index]
        else:
            for key2 in data2.keys():
                data1[key2][index]=data[key2][index]
    return data1, data2

def print_details(data, features, statistic_functions):
    for feature in features:
        print(feature)
        for func in statistic_functions:
            print(func(data[feature]), sep=" ,")




def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for func in statistic_functions:
        print(func(data[features[0]], data[features[1]]))