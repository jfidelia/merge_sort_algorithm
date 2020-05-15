Python program for implementation of MergeSort 
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i],end=" ") 
	print() 

# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7] 
	print ("Given array is", end="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr) 


# alist = [4, 1, 8, 2, 10, 3, 5, 9]
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        #print(alist)
        mergeSort(left)
        mergeSort(right)
        print(alist)


        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            # print(alist)
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
                # print(alist)
            k += 1
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
            # print(alist)
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
    print("Merging ",alist)

alist = [4,1,8,2,10,3,5,9]
mergeSort(alist)
print(alist)




