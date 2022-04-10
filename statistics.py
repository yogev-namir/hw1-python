from math import sqrt

def calc_mean(values):
    sum=0
    if len(values)==0:
        return 0
    for val in values:
        sum+=val
    return sum/len(values)

def calc_stdv(values):
    sum=0
    mean=calc_mean(values)
    if len(values) == 0:
        return 0
    for val in values:
        sum+=pow(val-mean)
    return sqrt(sum/(len(values)-1))

def calc_covariance(values1, values2):
    sum=0
    mean1=calc_mean(values1)
    mean2=calc_mean(values2)
    if len(values) == 0 | len(values2) == 0:
        return 0
    for val1,val2 in zip(values1,values2):
        sum=(val1-mean1)*(val2-mean2)
    return sum/(len(values1)-1)

def population_statistics(feature_description, data, treatment,
                          target, threshold, is_above,statistic_functions):
    