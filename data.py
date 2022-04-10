import pandas
def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient=”list”)
def filter_by_feature(data, feature, values):
def print_details(data, features, statistic_functions):
def print_joint_details(data, features, statistic_functions, statistic_functions_names):
