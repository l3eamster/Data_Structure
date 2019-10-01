# def countingSort(arr, exp1): 
  
#     n = len(arr) 
  
#     # The output array elements that will have sorted arr 
#     output = [0] * (n) 
  
#     # initialize count array as 0 
#     count = [0] * (10) 
  
#     # Store count of occurrences in count[] 
#     for i in range(0, n): 
#         index = (arr[i]/exp1) 
#         count[ (index)%10 ] += 1
  
#     # Change count[i] so that count[i] now contains actual 
#     #  position of this digit in output array 
#     for i in range(1,10): 
#         count[i] += count[i-1] 
  
#     # Build the output array 
#     i = n-1
#     while i>=0: 
#         index = (arr[i]/exp1) 
#         output[ count[ (index)%10 ] - 1] = arr[i] 
#         count[ (index)%10 ] -= 1
#         i -= 1
  
#     # Copying the output array to arr[], 
#     # so that arr now contains sorted numbers 
#     i = 0
#     for i in range(0,len(arr)): 
#         arr[i] = output[i] 
  
# # Method to do Radix Sort 
# def radixSort(arr): 
  
#     # Find the maximum number to know number of digits 
#     max1 = max(arr) 
  
#     # Do counting sort for every digit. Note that instead 
#     # of passing digit number, exp is passed. exp is 10^i 
#     # where i is current digit number 
#     exp = 1
#     while max1/exp > 0: 
#         countingSort(arr,exp) 
#         exp *= 10
  
# # Driver code to test above 
# arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
# radixSort(arr) 
  
# for i in range(len(arr)): 
#     print(arr[i]), 



def RadixSort(A):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for  i in A:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                A[a] = i
                a += 1
        placement *= RADIX
    return A
A = []
n = input("Enter the numebr of elements you want to sort : ")
n = int(n)
print("Enter the numbers : \n")
for i in range(0, n):
    num = int(input())
    A.append(num)
print(RadixSort(A))