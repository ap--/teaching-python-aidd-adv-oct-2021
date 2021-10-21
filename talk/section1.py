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
layer = [[row[0] for row in tbl] for tbl in data]



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
# === Memory Consumption === ?
import sys
print("sizeof 1", sys.getsizeof(1))
print(f"sizeof {2**(8*4) - 1}", sys.getsizeof(2**(8*4) - 1))
print(f"sizeof {2**(8*8) - 1}", sys.getsizeof(2**(8*8) - 1))
print(f"sizeof {2**(8*12) - 1}", sys.getsizeof(2**(8*12) - 1))
print(f"sizeof {2**(8*16) - 1}", sys.getsizeof(2**(8*16) - 1))

print("everything is an object", isinstance(0, object))



##
print("sizeof []", sys.getsizeof([]))
print(f"sizeof {[0]!r}", sys.getsizeof([0]))
print(f"sizeof {[0] * 2!r}", sys.getsizeof([0]*2))
print(f"sizeof {[0] * 3!r}", sys.getsizeof([0]*3))

# total = getsizeof([...]) + getsizeof(...every unique item in the list...)
# >>>     ~52 + N * 8      + N * PyObject



##
import numpy as np
arr = np.array(table)

print("arr", arr)
print("col1", arr[:, 1])
print("size of arr", sys.getsizeof(arr), "\n")

print("size of []", sys.getsizeof(np.array([], dtype=int)))
print("size of [1]", sys.getsizeof(np.array([1], dtype=int)))
print("size of [1,1]", sys.getsizeof(np.array([1, 1], dtype=int)))



##
# what extra information is stored in the array ?

def array_info(a):
    from pprint import pformat
    for attr in ['size', 'dtype', 'ndim', 'shape', 'strides', 'flags']:
        print(f"array.{attr}", pformat(getattr(a, attr)))

print(arr)
array_info(arr)



##
# how is the data stored in memory?
"""
| v00 | v01 | v02 |
| v10 | v11 | v12 |
| v20 | v21 | v22 |
"""

# | v00 | v01 | v02 | v10 | v11 | v12 | v20 | v21 | v22 |
# <---------------------- size = 9 --------------------->  # size
# <- 8 -> bytes                                            # dtype
# <------- 24 ------> bytes                                # strides[0]
# <- 8 -> bytes                                            # strides[1]

# from arr[0, 0] to arr[0, 1] advance 8 bytes
# from arr[0, 0] to arr[1, 0] advance 24 bytes



##
# reshaping an array changes the shape, ndim, strides
flat_array = arr.reshape((-1,))
array_info(flat_array)
print(flat_array)



##
# the underlying data can be viewed as different dtypes
flat_array_as_bytes = flat_array.view(dtype=np.uint8)
array_info(flat_array_as_bytes)
print(flat_array_as_bytes)



##
# numpy operations that take advantage of creating views
arr = np.array([[1, 2, 3], [10, 20, 30]])
array_info(arr)
transposed = arr.T
array_info(transposed)  # transposed is just a view of the original

# ensure copy
a_copy = arr.copy()


##
# === Tricks you can do with strides ===

# repeating an array in memory
data = np.arange(4, dtype=int)
array_info(data)
print(data)

def repeat(a, n):
    return np.lib.stride_tricks.as_strided(
        a,
        shape=(n, ) + a.shape,
        strides=(0, ) + a.strides,
    )

repeated = repeat(data, 6)



##
# sliding window
data = np.arange(8, dtype=int)

def sliding_window(a, window_size):
    assert a.ndim == 1
    num_of_windows = a.size - window_size + 1
    new_strides = (a.strides[0], a.strides[0])
    return np.lib.stride_tricks.as_strided(
        a,
        shape=(num_of_windows, window_size),
        strides=new_strides
    )

sw = sliding_window(data, 3)



##
# === NUMPY TAKE HOME MESSAGE ===

arr = np.array([123]*100)
# arr.shape, arr.ndim, arr.dtype, arr.strides

# be aware of views vs copies:
view_of_arr_if_possible = arr.reshape(10, 10)

# can do fancy things by changing the strides
np.lib.stride_tricks.as_strided(...)

# goto: https://numpy.org/learn/
