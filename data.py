import pandas


def filter_by_feature(data, feature, values):
    """
        :param data: full dictionary from the Excel file
        :param feature: the desire key, a string
        :param values: a set of numbers. A range of achievable values
        :return: two dictionaries, one with the required values and the other with the complementary values
    """
    dict_1 = {}
    dict_2 = {}
    values_of_feature = [0 if a == values else 1 for a in data.get(feature)]
    for key in data:
        d1_key_value = []
        d2_key_value = []
        for i in range(len(values_of_feature)):
            # checks for each item which dictionary is appropriate for him
            d2_key_value.append(data.get(key)[i]) if values_of_feature[i] else d1_key_value.append(data.get(key)[i])
        dict_1.update({key: d1_key_value})
        dict_2.update({key: d2_key_value})
    return dict_1, dict_2


def print_details(data, features, statistic_functions):
    """
    :param data: a dictionary of numbers
    :param features: a list of required features(keys) to print
    :param statistic_functions: a list of functions from statistics.py, an attached file
    :return: prints the returned values from the statistics.py functions for each given feature
    """
    for feature in features:
        outputs = []
        for func in statistic_functions:
            output = f"{func(data.get(feature)):.2f}"
            outputs.append(str(output))
        print(f'{feature}: ' + ', '.join(outputs))


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for func in statistic_functions:
        output = f"{func(data.get(features[0]), data.get(features[1])):.2f}"
        print(statistic_functions_names+"("+f'{features[0]}, {features[1]}'+"): "+output)


def load_data(path, features):
    """
        gets a file's path and returns a dict- it's keys are the features givens
        and their value are given in the file
        :param path: the file's path
        :param features: the relevant features to save
        :return: a dict with the suitable keys and values
        """
    data = {}
    df = pandas.read_csv(path)
    data_raw = df.to_dict(orient="list")
    for key in data_raw.keys():
        if key in features:
            data[key] = data_raw[key]
    return data
