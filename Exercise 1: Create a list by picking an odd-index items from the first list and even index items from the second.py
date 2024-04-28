# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

# Given:

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]

# Expected Output:

# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]

# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]


def pickingNumber(list1:list, list2:list):
    list3:list = list1[1::2]+list2[0::2]
    #list3.append(list1[1::2])
    #list3.append(list2[0::2])
    print("Element at odd-index positions from list one")
    print(list1[1::2])
    print("Element at even-index positions from list two")
    print(list2[0::2])
    print("Printing Final third list")
    print(list3)

def main():
    list1:list = [3, 6, 9, 12, 15, 18, 21]
    list2:list = [4, 8, 12, 16, 20, 24, 28]
    pickingNumber(list1,list2)
if __name__=="__main__":
    main()