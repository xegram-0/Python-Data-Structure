# Exercise 4: Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

# Given:

# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Expected Output:

# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

def count_occurrence(sample_list:list):
    listDict:dict = dict()
    for item in sample_list:
        if item in listDict:
            listDict[item] += 1
        else:
            listDict[item] = 1
    #print(listDict)
    print(f"Printing count of each item {listDict}")

def main():
    sample_list:list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    count_occurrence(sample_list)
if __name__=="__main__":
    main()

