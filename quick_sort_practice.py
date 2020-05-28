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

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [88,55,99,33,22,14,15,2,3,6,7]
print(alist)
quickSort(alist)
print(alist)