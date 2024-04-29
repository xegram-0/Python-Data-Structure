# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:

# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Expected Outcome:

# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

def chunk_and_reverse(sample_list:list):
    chunkSize:int = len(sample_list)//3
    tempList:list = []
    start:int = 0
    end:int = chunkSize
    #print(chunkSize)
    for i in range(chunkSize):
        index = slice(start,end)
        tempList = sample_list[index]
        
        print(f"Chunk number {i} is {tempList}")
        print(f"Its reversed list is {list(reversed(tempList))}")
        #print((reversed(tempList))) results in list object
        start = end
        end += chunkSize

def main():
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    chunk_and_reverse(sample_list)

if __name__=="__main__":
    main()