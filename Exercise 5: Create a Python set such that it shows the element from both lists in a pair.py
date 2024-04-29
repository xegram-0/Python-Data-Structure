# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# Given:

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# Expected Output:

# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

def create_set(first_list:list,second_list:list):
    joined_list:set = set(zip(first_list,second_list))

    print(f"Result is {joined_list}")

def main():
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    create_set(first_list,second_list)
if __name__=="__main__":
    main()