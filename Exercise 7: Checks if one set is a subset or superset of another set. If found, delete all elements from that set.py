# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Given:

# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

# Expected Output:

# First set is subset of second set - True
# Second set is subset of First set -  False

# First set is Super set of second set -  False
# Second set is Super set of First set -  True

# First Set  set()
# Second Set  {67, 73, 43, 48, 83, 57, 29}

def check_set(first_set:set, second_set:set):

    print(f"Is first set subset of second set? {first_set.issubset(second_set)}")
    print(f"Is second set subset of first set? {second_set.issubset(first_set)}")
    print(f"Is first set superset of second set? {first_set.issuperset(second_set)}")
    print(f"Is second set superset of first set? {second_set.issuperset(first_set)}")

    if first_set.issubset(second_set):
        # printing this code would result in console telling "None"
        first_set.clear()
    if second_set.issubset(first_set):
        second_set.clear()
    print("\n")
    print(f"The first set {first_set}")
    print(f"The second set {second_set}")

def main():
    first_set = {27, 43, 34}
    second_set = {34, 93, 22, 27, 43, 53, 48}
    check_set(first_set,second_set)

if __name__=="__main__":
    main()