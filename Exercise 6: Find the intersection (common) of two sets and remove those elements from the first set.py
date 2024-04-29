# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# Given:

# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# Expected Output:

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

def intersection_remove(first_set:set,second_set:set):

    result_set:set = first_set.intersection(second_set)
    print(f"Intersection is {result_set}")
    for num in result_set:
        first_set.remove(num)
    print(f"First set after removing common elements: {first_set}")

def main():
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    intersection_remove(first_set,second_set)

if __name__=="__main__":
    main()