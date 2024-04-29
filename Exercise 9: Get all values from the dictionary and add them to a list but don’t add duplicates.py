# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:

# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Expected Outcome:

# [47, 52, 44, 53, 54]
def get_value(speed:dict):
    valueList:list = list(dict.fromkeys(speed.values()))
    print(f"The result: {valueList}")

    # for val in speed.values():
    # check if value not present in a list
    # if val not in speed_list:
    #     speed_list.append(val)
def main():
    speed = {'jan': 47, 
             'feb': 52, 
             'march': 47, 
             'April': 44, 
             'May': 52, 
             'June': 53, 
             'july': 54, 
             'Aug': 44, 
             'Sept': 54}
    
    get_value(speed)
if __name__=="__main__":
    main()