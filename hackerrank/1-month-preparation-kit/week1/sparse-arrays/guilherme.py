from collections import Counter
def matchingStrings(strings, queries):
    # Write your code here
    count_strings = Counter(strings)
    result = []
    for q in queries:
        result.append(count_strings[q])

    return result


assert matchingStrings(['ab','ab','abc'], ['ab','abc','bc']) == [2,1,0]
assert matchingStrings(['a']*100 + ['ab'] *200 + ['abc']*300, ['a','ab','abc']) == [100,200,300]