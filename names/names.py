import time
from bst import Binary_Search_Tree
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

