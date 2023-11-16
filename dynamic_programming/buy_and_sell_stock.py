# Buy and sell the stock only once
from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    mn = prices[0]
    profit = 0
    n = len(prices)
    for i in range(1,n):
        if prices[i]>mn:
            profit = max(profit, prices[i]-mn)
        else:
            mn = prices[i]
    return profit


