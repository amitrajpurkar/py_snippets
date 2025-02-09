import timeit

my_set={1,2,3,4,5}
def set_lookup():
    return 5 in my_set


my_dict={1:"a",2:"b",3:"c",4:"d",5:"e"}
def dict_lookup():
    return 5 in my_dict


# measure the execution time of the set lookup
set_time = timeit.timeit(set_lookup, number=1000000)
print(f"Set lookup time: {set_time} seconds")

# measure the execution time of the dict lookup
dict_time = timeit.timeit(dict_lookup, number=1000000)
print(f"Dict lookup time: {dict_time} seconds")

