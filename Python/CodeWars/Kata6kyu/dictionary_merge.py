"""Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.

The keys in the given dictionaries can overlap. In that case you should combine all source values in an array. Duplicate values should be preserved."""


def merge(*dicts):
    keylist = []

    for dictionary in dicts:
        for key in dictionary:
            keylist.append(key)

    answer = {}

    for key in keylist:
        answer[key] = []

        for dictionary in dicts:
            if key in dictionary:

                answer[key].append(dictionary[key])

    return answer


if __name__ == '__main__':

    assert merge({}, {}, {}) == {}

    #"Merge_Single_Dictionary_Returns_Dictionary_With_Same_Content"
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}

    #"Merge_Two_Simple_Dictionaries_Returns_Combined_Dictionary"
    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}

    #"Merge_Two_Dictionaries_With_Multiple_Values_Returns_Combined_Dictionary"
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {
        "A": [1, 4], "B": [2], "C": [3], "D": [5]}
