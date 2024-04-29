# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# Expected Outcome:

# After removing unwanted elements from list [47, 69, 76, 97]

def check_and_remove(roll_number:list,sample_dict:dict):
    # for num in roll_number:
    #     for value in sample_dict:
    #         if num == sample_dict[value]:
    #             continue
    #         else:
    #             roll_number.dicard(num)
    #             pass
    # https://stackoverflow.com/questions/21510140/best-way-to-remove-elements-from-a-list
    # Guess it is only list comprehension can do the job
    roll_number = [number for number in roll_number if number in sample_dict.values()]
    print(f"After removing number: {roll_number}")

def main():
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    check_and_remove(roll_number,sample_dict)

if __name__=="__main__":
    main()

