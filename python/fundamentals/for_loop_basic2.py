# 1  Biggie Size
# def Biggie_size(arr):
#     for i in range (0,len(arr),1):
#         if arr[i] > 0:
#             arr[i] = "big"
#     return arr


# print (Biggie_size([-1,3,5,-5]))


# 2 Count Positives
# def count_positives(arr):
#     count = 0
#     for i in range (0,len(arr),1):
#         if arr[i]>0:
#             count += 1
#     arr[len(arr) - 1] = count
#     return arr


# print(count_positives([-1,1,1,1]))


# 3 Sum Total
# def sum_total(arr):
#     sum = 0
#     for i in range (0,len(arr),1):
#         sum += arr[i]
#     return sum

# print(sum_total([1,2,3,4]))


# 4 Average
# def sum_total(arr):
#     sum = 0
#     for i in range (0,len(arr),1):
#         sum += arr[i]
#     return sum / len(arr)

# print(sum_total([1,2,3,4]))


# 5 Length
# def length(arr):
#     return len(arr)


# print(length([37,2,1,-9]))


# 6 Minimum
# def minimum(arr):
#     if len(arr) == 0:
#         return False
#     min = arr[0]
#     for i in range (0,len(arr),1):
#         if min > arr[i]:
#             min = arr[i]
#     return min

# print(minimum([]))    


# 7 Maximum
# def maximum(arr):
#     if len(arr) == 0:
#         return False
#     max = arr[0]
#     for i in range (0,len(arr),1):
#         if max < arr[i]:
#             max = arr[i]
#     return max

# print(maximum([37,2,1,-9]))

# # 8 Ultimate Analysis
# def  ultimate_analysis(arr):
#     analysis = {}
#     sum = 0
#     min = arr[0]
#     max = arr[0]
#     for i in range (0,len(arr),1):
#         sum += arr[i]
#         if min > arr[i]:
#             min = arr[i]
#         if max < arr[i]:
#             max = arr[i]
#     average = sum / len(arr)
#     analysis = {'sumTotal': sum, 'averageTotal': average, 'minimum': min, 'maximum': max, 'length': len(arr)}
#     return analysis

# print(ultimate_analysis([37,2,1,-9]))




# 9 Reverse
# def reverseList(arr):
#   newarr = []

#   for i in range (len(arr) -1, -1, -1):
#     newarr.append(arr[i])
#   return newarr

# print(reverseList([37, 2, 1, -9]))


# def reverse_list(list):
#     for index in range(round(len(list)/2)):
#         list[index], list[len(list)-index-1] = list[len(list)-1-index], list[index]
#     return list

# print(reverse_list([9,6,5,4]))