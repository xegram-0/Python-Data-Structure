# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

# Given:

# list1 = [54, 44, 27, 79, 91, 41]

# Expected Output:

# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]


def remove_add(list1:list):
    removed_value:int = list1.pop(4)
    print(list1)
    list1.insert(2, removed_value)
    print(list1)
    # append() would put value at the exact the end
    # while insert(-1) would place before last position
    list1.append(removed_value)
    print(list1)

def main():
    list1:list = [54, 44, 27, 79, 91, 41]
    remove_add(list1)

if __name__=="__main__":
    main()