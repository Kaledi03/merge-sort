import random

"""

    Implementation of the Merge sort algorythm by Kaled Brahmi

"""

# In order to use the code you can change the constants below and run the code
NUM = 10 # Number of elements with wich will the list be populated
MIN_NUM = 0  # Smallest number that will populate the list
MAX_NUM = 100  # Heighest number that will populate the list

def main():
    arr = []
    # Populating the list with NUM elements in the range MIN_NUM - MAX_NUM
    for i in range(NUM):
        arr.append(random.randint(MIN_NUM, MAX_NUM))

    # Print the unsorted list
    print("Unsorted array: ")
    printArr(arr)

    # Assign the value returned by the recursive function 'sort' to the variable 'sortedArr'
    sortedArr = sort(arr, 0, len(arr)-1)

    # Print the sorted list
    print("Sorted array: ")
    printArr(sortedArr)

def printArr(arr):
    for i in range(len(arr)):
        print("\t" + str(arr[i]))

# Recurseive function that returns a sorted list
def sort(arr, start, end):
    returnArr = []

    # Base case of the function trigered when the array is completly divided
    if start >= end:
        returnArr.append(arr[start])
    else:
        arrLeft = sort(arr, start, int((end-start)/2)+start)
        arrRight = sort(arr, (int((end-start)/2)+1+start), end)
        returnArr = merge(arrLeft, arrRight)
    return returnArr

# Function used by the 'sort' function used to add the two sorted half of the sub-lists
def merge(arrLeft, arrRight):
    i = 0
    j = 0
    returnArr = []
    while len(returnArr) < len(arrLeft) + len(arrRight):
        if i == (len(arrLeft)):
            for k in range(j, len(arrRight)):
                returnArr.append(arrRight[k])
            return returnArr
        elif j == (len(arrRight)):
            for k in range(i, len(arrLeft)):
                returnArr.append(arrLeft[k])
            return returnArr

        if arrLeft[i] > arrRight[j]:
            returnArr.append(arrRight[j])
            j += 1
        else:
            returnArr.append(arrLeft[i])
            i += 1

    return returnArr



if __name__ == "__main__":
    main()
