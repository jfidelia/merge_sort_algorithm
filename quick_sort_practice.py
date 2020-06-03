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

    lefthelper = first + 1
    righthelper = last

    done = False
    while not done:

        while lefthelper <= righthelper and alist[lefthelper] <= pivotvalue:
            lefthelper = lefthelper + 1

        while alist[righthelper] >= pivotvalue and righthelper >= lefthelper:
            righthelper = righthelper - 1

        if righthelper < lefthelper:
            done = True
        else:
            temp = alist[lefthelper]
            alist[lefthelper] = alist[righthelper]
            alist[righthelper] = temp

    temp = alist[first]
    alist[first] = alist[righthelper]
    alist[righthelper] = temp

    return righthelper

alist = [989,777,999,454,676,323,878,676,321,1,3,10,20,19,9,6,32,44,68,97,200,342,568,435,543]
print(alist)
quickSort(alist)
print(alist)

        
     