
# def quickSort(alist):
#     quickSortHelper(alist, 0, len(alist) - 1)
#     #print(quickSort)

# def quickSortHelper(alist, first, last):
#     if first < last:
        
#         splitpoint = partition(alist,first,last)
        
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

# new_list = [3,55,6,2,8,19,33]
# print(new_list)
# quickSort(new_list)
# print(new_list) 