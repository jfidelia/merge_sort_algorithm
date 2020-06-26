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

        while leftmarker <= rightmarker and alist[leftmarker] <= pivotvalue:
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

alist = [55,66,7,88,9,45,36,21,38,98,34,67,1,3]
print(alist)
quickSort(alist)
print(alist)