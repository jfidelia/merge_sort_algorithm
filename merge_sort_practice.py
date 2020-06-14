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

def mergeSort(alist):
    print("Splitting ", alist)
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

    print("Merging ", alist)

alist = [66,77,88,99,200,44,22,11,1,4,6,8]
mergeSort(alist)
print(alist)