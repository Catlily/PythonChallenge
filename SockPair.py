#John works at a clothing store. He has a large pile of socks that he must pair
#by color for sale. Given an array of integers representing the color of each 
#sock, determine how many pairs of socks with matching colors there are.
#For example, there are  socks with colors . There is one pair of color and 
#one of color . There are three odd socks left, one of each color. 
#The number of pairs is 2.
#n: the number of socks in the pile
#ar: the colors of each sock
import math
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    try:
        1<= n <= 100
    except:
        print('Error: n is not in range')
    counter = collections.Counter(ar)
    value_ls = counter.values()
    pair_num = []
    for value in value_ls:
        pair_num.append(math.trunc(value/2))
    result = sum(pair_num)
    return result

n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)