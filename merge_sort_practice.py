# def mergeSort(alist):
#     print("splitting", alist)
#     if len(alist) > 1:
#         mid = len(alist) // 2
#         left = alist[:mid]
#         right = alist[mid:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right [j]:
#                 alist[k] = left [i]
#                 i += 1
#             else:
#                 alist[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             alist[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             alist[k] = right[j]
#             j += 1
#             k += 1
#     print("Merging", alist)

# alist = [22,3,15,17,2,10,19,13]
# mergeSort(alist)
# print(alist)

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):

    pivotvalue = alist[first]

    leftmarker = first + 1
    rightmarker = last

    done = False
    while not done:

        while leftmarker <= rightmarker and alist [leftmarker] <= pivotvalue:
            leftmarker = leftmarker + 1

        while alist[rightmarker] >= pivotvalue and rightmarker >= leftmarker:
            rightmarker = rightmarker - 1

        if rightmarker < leftmarker:
            done = True
        else:
            temp = alist[leftmarker]
            alist[leftmarker] = alist[rightmarker]
            alist[rightmarker] = temp

    temp = alist[first]
    alist[first] = alist[rightmarker]
    alist[rightmarker] = temp

    return rightmarker

alist = [66,77,33,12,10,23,1,7,100,76,65,44,99,75,9]
print(alist)
quickSort(alist)
print(alist)