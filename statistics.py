from math import sqrt
from data import filter_by_feature


def calc_mean(values):
    sum = 0
    if len(values) == 0:
        return 0
    for val in values:
        sum += val
    return sum / len(values)


def calc_stdv(values):
    sum = 0
    mean = calc_mean(values)
    if len(values) == 0:
        return 0
    for val in values:
        sum += ((val - mean) ** 2)
    return sqrt(sum / (len(values) - 1))


def calc_covariance(values1, values2):
    sum = 0
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)
    if len(values1) == 0 | len(values2) == 0:
        return 0
    for val1, val2 in zip(values1, values2):
        sum += (val1 - mean1) * (val2 - mean2)
    return sum / (len(values1) - 1)


def population_statistics(feature_description, data, treatment,
                          target, threshold, is_above, statistic_functions):
    """
        :param feature_description: an opening line that explain the following data source
        :param data: fixed dictionary, according to the desire feature
        :param treatment: a key that we check the threshold on his values, a string
        :param target: a key that we apply the statistic function on it's values, after filtering them
        :param threshold: an integer that split the range of values to two, larger\smaller(or equal) than it
        :param is_above: 1 or 0, check "above" the threshold or under
        :param statistic_functions: a list of functions from statistics.py, an attached file
        :return: a string contains the statistic data(sum,mean,median) of the desire feature's values
        """
    if is_above:
        data["threshold"] = [1 if a > threshold else 0 for a in data.get(treatment)]
    else:
        data["threshold"] = [0 if a <= threshold else 1 for a in data.get(treatment)]
    dict_above, dict_below = filter_by_feature(data, "threshold", is_above)
    print(f"{feature_description}")
    outputs = []
    for func in statistic_functions:
        output = f"{func(dict_above.get(target)):.2f}"
        outputs.append(str(output))
    print(f'{target}: ' + ', '.join(outputs))