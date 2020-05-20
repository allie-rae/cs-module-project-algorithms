'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # if the number has a duplicate, ignore
    # if the number does not have a duplicate, return it 
    # each each item in array against each other item in the 
    # array except itself
    num = arr[0]
    for i in range(1,len(arr)):
        num = num ^ arr[i]
    return num
    
    # uses exclusive or operator 
    # returns like:
    # 9 ^ (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)
    # = 9 ^ 0 ^ 0 ^ 0 ^ 0 ^ 0
    # = 9 ^ 0 
    # = 9
    # Because: XOR of a num with itself is 0. 
    # But XOR of a num by itself is the num. 

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")