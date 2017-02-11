# /bin/python
'''
    Given a list of integers, and a total k, return the pairs that derive k
    If no pairs are found, then return None
    Think of it as having 10 pounds / dollars / euro in your pocket, and wanting
    to buy 2 items that equal that exact amount from a list of items

    Complexity is O(n) - thanks to the use of a dictionary and hashing

    :param int  k       The total value we're looking for
    :param list aList   The list of integers to derive pairs from
'''
def find(k, aList):
    # make the keys of the dictionary the values from aList
    ref = {value : key for (key, value) in enumerate(aList)}
    pairs = []
    # for each of the keys, look for k - key in the dictionary
    # Look ups are carried out in constant time O(1)
    for key in ref.keys():
        if ref.get(k - key) is not None:
            pairs.append((key, k-key))
            del ref[key] # This prevents duplicates
    return pairs if len(pairs) > 0 else None
