# from bs4 import BeautifulSoup
# import requests
# import nltk
# # from tqdm.noteboo import tqdm
# from nltk.sentiment import SentimentIntensityAnalyzer
# si = SentimentIntensityAnalyzer()
# from pathlib import Path
# import csv
# import  openpyxl

# data = {"name":100}
# file = open('d.csv',"w")
# writer = csv.writer(file)
# writer.writerow(data.values())
# # writer.writerow("\n")
# writer.writerow("sdjadjaldja")

# import math

# def maxSubarrayValue(arr):
#     n = 0
#     j = 1
#     evens = [0]
#     odds = [0]
#     while n < math.ceil(len(arr)/2):
#         evens[0] = evens[0]+arr[2*n]
#         n=n+1
#     while j < math.ceil(len(arr)/2):
#         odds[0] = odds[0]+arr[(2*j)-1]
#         j = j+1
#     return (evens[0]- odds[0])**2
# s = list(input(""))
# s.pop(0)
# array = []
# z = 0
# for i in s:
#     if i == "-":
#         data = s[z+1]
#         array.append(-int(data))
#         s.pop(z+1)
#         z=z+1
#     else:
#         array.append(int(i))
#         z=z+1
# print(maxSubarrayValue(array))

def arrayManipulation(n, queries):
    j = 0
    z=0
    arr = []
    for  i in range(n):
        arr.append(0)
    print(queries[j][z],queries[j][z+1])
    while j < 3:
        for i in range(queries[j][z],queries[j][z+1]+1):
            arr[i-1]= arr[i-1]+queries[j][z+2]
        j = j+1
    return arr
n=10
queries = [[1,5,3],[4,8,7],[6,9,1]]

print(arrayManipulation(n,queries))
