import sys

def main(argv):
    # loading the csv, the statistic functions and features for the program
    str_input = argv[2]
    features: list = str_input.split(", ")
    dictionary = data.load_data(argv[1], features)
    statistic_functions = [statistics.sum, statistics.mean ]
    continuous_features = features[:3]
    """
    ##############################~~QUESTION 1~~###################################
    holder are just spare dictionaries to store the second returned dictionary,
    they are not being used during the program
    """
    data_summer, holder = data.filter_by_feature(dictionary, features[3], SUMMER)
    data_holiday, holder = data.filter_by_feature(dictionary, features[4], HOLIDAY)
    print(f"Question 1:")
    print(f"Summer:")
    data.print_details(data_summer, continuous_features, statistic_functions)
    print(f"Holiday:")
    data.print_details(data_holiday, continuous_features, statistic_functions)
    print(f"All:")
    data.print_details(dictionary, continuous_features, statistic_functions)
    """
    ############################~~QUESTION 2~~###############################
    """
    descriptions = ["Winter holiday records:", "Winter weekday records:"]
    data_winter, holder = data.filter_by_feature(dictionary, features[3], WINTER)
    new_data_holiday, data_weekday = data.filter_by_feature(data_winter, features[4], HOLIDAY)
    list_of_dictionaries = [new_data_holiday, data_weekday]
    new_statistic_functions = [statistics.mean, statistics.median]
    signs_list = ["<=", ">"]

    print(f"\nQuestion 2:")
    for i in range(SECTIONS):
        print(f"If {features[1]}{signs_list[i]}13.0, then:")
        for j in range(SECTIONS):
            data.population_statistics(descriptions[j],
                                       list_of_dictionaries[j], features[1], features[2],
                                       THRESHOLD, i, new_statistic_functions)


if __name__ == '__main__':
    main(sys.argv)

