# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# Expected Outcome:

# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

def remove_duplicate(sample_list:list):
    sample_list = list(dict.fromkeys(sample_list))
    return sample_list
    # sample_list = list(set(sample_list))

def create_tuple(newList:list):
    tupleList = tuple(newList)
    return tupleList

def main():
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    newList:list = remove_duplicate(sample_list)
    tupleList:tuple = create_tuple(newList)
    print(newList)
    print(create_tuple(newList))
    print(min(tupleList))
    print(max(tupleList))

if __name__=="__main__":
    main()