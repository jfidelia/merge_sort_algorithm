# def quickSort(alist):
#     quickSortHelper(alist, 0, len(alist) - 1)

# def quickSortHelper(alist, first, last):
#     if first < last:

#         splitpoint = partition(alist, first, last)

#         quickSortHelper(alist, first, splitpoint - 1)
#         quickSortHelper(alist, splitpoint + 1, last)

# def partition(alist, first, last):
#     pivotvalue = alist[first]

#     leftmark = first + 1
#     rightmark = last

#     done = False
#     while not done:

#         while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1
#             print(alist)

#         while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark - 1
#             print(alist)

#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = alist[leftmark]
#             alist[leftmark] = alist[rightmark]
#             alist[rightmark] = temp

#     temp = alist[first]
#     alist[first] = alist[rightmark]
#     alist[rightmark] = temp
    
#     return rightmark

# alist = [77,55,99,1,4,22,18,10,15]
# print(alist)
# quickSort(alist)
# print(alist)

# def quickSort(alist):
#     quickSortHelper(alist, 0, len(alist) - 1)

# def quickSortHelper(alist, first, last):
#     if first < last:

#         splitpoint = partition(alist, first, last)

#         quickSortHelper(alist, first, splitpoint - 1)
#         quickSortHelper(alist, splitpoint + 1, last)

# def partition(alist, first, last):

#     pivotvalue = alist[first]

#     leftmark = first + 1
#     rightmark = last 

#     done = False
#     while not done:
#         while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1

#         while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark - 1

#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = alist[leftmark]
#             alist[leftmark] = alist[rightmark]
#             alist[rightmark] = temp

#     temp = alist[first]
#     alist[first] = alist[rightmark]
#     alist[rightmark] = temp

#     return rightmark

# alist = [66,44,77,33,43,23,12,99,88,2000,201,2001,1500]
# print(alist)
# quickSort(alist)
# print(alist)

def mergeSort(alist):
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    print("Merging", alist)

alist = [77,33,55,0,1,99,88,1000,3000]
mergeSort(alist)
print(alist)