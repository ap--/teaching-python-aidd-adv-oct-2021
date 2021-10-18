"""
    ███    ██ ██    ██ ███    ███ ██████  ██    ██
    ████   ██ ██    ██ ████  ████ ██   ██  ██  ██  
    ██ ██  ██ ██    ██ ██ ████ ██ ██████    ████   
    ██  ██ ██ ██    ██ ██  ██  ██ ██         ██    
    ██   ████  ██████  ██      ██ ██         ██
"""
# basic example: how do we store tabular data in python?

#   | sample1 | sample2 | sample3 |
#   |---------|---------|---------|
#   |     100 |    1024 |       0 |  <-- experiment1
#   |     200 |    2048 |       1 |  <-- experiment2
#   |     300 |    4096 |       2 |  <-- experiment3


##
# let's store the tabular data as lists of lists of values
row0 = [100, 1024, 0]
row1 = [200, 2048, 1]
row2 = [300, 4096, 2]
table = [row0, row1, row2]


##
# accessing single elements or columns?
x = table[1][1]
col1 = [row[1] for row in table]


##
# what about a subsection of the table?
subtable = [row[1:] for row in table[1:]]


##
# how does this look for 3D data?
row00 = [1, 2]
row01 = [3, 4]
row10 = [5, 6]
row11 = [7, 8]
table0 = [row00, row01]
table1 = [row10, row11]
data = [table0, table1]
# selection:
x = data[1][1][1]
layer = [row[0] for table in data for row in table]


##
from collections import UserList

class BadArray(UserList):
    def __getitem__(self, item):
        def _ndidx(data, item):
            if isinstance(item, (int, slice)):
                return data[item]
            elif isinstance(item, tuple):
                j, i = item[0], item[1:]
                return _ndidx([_ndidx(d, i) if i else d for d in data], j)
            else:
                raise TypeError(type(item).__name__)
        data = _ndidx(self.data, item)
        return BadArray(data) if isinstance(data, list) else data

arr = BadArray(data)
print(arr[:, 1, :])


##
import numpy as np
arr = np.array(data)



