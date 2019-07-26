import time
from bst import Binary_Search_Tree
from arraybst import Binary_Array
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

tree = Binary_Search_Tree(names_1[0])
duplicates = []
for name_1 in names_1[1:]:
    tree.add(name_1)
for name_2 in names_2:
    if tree.search(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

print("Second pass solution below")



"""
OPTIMIZED SOLUTION HERE
"""


new_time = time.time()
f = open('names_1.txt', 'r')
first_names = f.read().split("\n")
f.close

f = open('names_2.txt', 'r')
second_names = f.read().split("\n")
f.close

name_dict = {}
duplicate_list = []

for first_name in first_names:
    name_dict[first_name] = 1
for second_name in second_names:
    if name_dict.get(second_name) is not None:
        duplicate_list.append(second_name)

new_end = time.time()
print (f"{len(duplicate_list)} duplicates:\n\n{', '.join(duplicate_list)}\n\n")
print (f"runtime: {new_end - new_time} seconds")



"""
ARRAY ONLY SOLUTION HERE
"""

# array_time = time.time()

# f = open('names_1.txt', 'r')
# array_first_names = f.read().split("\n")
# f.close()

# f = open('names_2.txt', 'r')
# array_second_names = f.read().split("\n")
# f.close()

# binary_heap = Binary_Array(len(array_first_names))
# binary_heap_array = []
# i = 0
# for name1 in array_first_names:
#         print(f"Adding name number {i}")
#         i += 1
#         binary_heap.add(name1)

# for name2 in array_second_names:
#         if binary_heap.search(name2):
#                 binary_heap_array.append(name2)

# array_end = time.time()
# print (f"{len(binary_heap_array)} duplicates:\n\n{', '.join(binary_heap_array)}\n\n")
# print (f"runtime: {array_end - array_time} seconds")