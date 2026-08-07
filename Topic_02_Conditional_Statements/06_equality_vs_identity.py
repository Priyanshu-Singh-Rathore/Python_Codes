# Question 6:
# Demonstrate the difference between == and is by comparing two lists
# with the same contents.

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list1 == list2: {list1 == list2}")  # True: same contents/values
print(f"list1 is list2: {list1 is list2}")  # False: different objects in memory
print(f"id(list1): {id(list1)}")
print(f"id(list2): {id(list2)}")

# For comparison, assigning list2 to reference list1 makes 'is' True too:
list3 = list1
print(f"list1 is list3: {list1 is list3}")  # True: same object

# Time Complexity: O(n)
# Space Complexity: O(1)
