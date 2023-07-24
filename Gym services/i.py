from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

chain_map = ChainMap(dict1, dict2, dict3)
print(chain_map['a'])  # Output: 1
print(chain_map['b'])  # Output: 2 (from dict1)
print(chain_map['c'])  # Output: 4 (from dict2)
print(chain_map['d'])  # Output: 6 (from dict3)


