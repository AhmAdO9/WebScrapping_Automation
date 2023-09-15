# K = [[7, 867],
# [7,6429964,4173738,9941618,2744666,5392018,5813128,9452095],
# [7,6517823,4135421,6418713,9924958,9370532,7940650,2027017],
# [7,1506500,3460933,1550284,3679489,4538773,5216621,5645660],
# [7,7443563,5181142,8804416,8726696,5358847,7155276,4433125],
# [7,2230555,3920370,7851992,1176871,610460,309961,3921536],
# [7,8518829,8639441,3373630,5036651,5291213,2308694,7477960],
# [7,7178097,249343,9504976,8684596,6226627,1055259,4880436]]
# li = [0]
# for i in K:
#    li[0] = li[0]+((max(i))**2)
# print(li[0])
# for i in range(1,1001):    
#     if li[0]%i == 866:
#         print(li[0]%i)
#         print(i)
#         break

# print(533370066369154 % 976)
# 
# def findSubstring(s, k):
#     li = {}
#     ori = k
#     j=0
#     l = len(s)
#     new = s[:k]
#     while j <= l-3:
#         num = [0]
#         comp = {'a','e','i','o','u'}
#         for i in new:
#             if i in comp:
#                 num[0]=num[0]+1
#         li[num[0]]=new
#         j=j+1
#         k=k+1
#         new = s[j:k]
#         if len(new) == ori:
#             continue
#         else:
#            return li   
     
  

# print(findSubstring("kjsancerdiilldnsflknaaskdlakowqjdkjser",7))


# def sum(x):
#     if x >= 10:
#         return x
#     x+=1
#     s = sum(x)
#     return s+2
# print(sum(0))

# class Car:
#     def __init__(self, speed, unit):
#         self.max_speed = speed,
#         self.unit = unit
#         print("Car with the maximum speed of",str(speed)+unit)
             
 
# class Boat:
#     def __init__(self, speed):
#         self.max_speed = speed,
#         print("Boat with the maximum speed of",str(speed)+"knots")

# sp = input("")
# new = sp.split(" ")
# if new[0] == 'car':
#     car = Car(new[1], new[2])
# else:
#     boat = Boat(new[1])

arr = [1,2,3,4,5]
print(arr[1:4])