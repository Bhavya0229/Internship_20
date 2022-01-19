"""
Task
Given an array, X, of N integers and an array, W, representing the respective weights of X‘s elements, calculate and print the weighted mean of X‘s elements. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

Example

X = [1, 2, 3]
W = [5, 6, 7]
The array of values X[i] * W[i] = [5, 12, 21]. Their sum is 38. The sum of W = 18. The weighted mean is 38/18 = 2.1111. . . . Print 2.1 and return.

Function Description
Complete the weightedMean function in the editor below.

weightedMean has the following parameters:
– int X[N]: an array of values
– int W[N]: an array of weights

Prints
– float: the weighted mean to one decimal place

Input Format
The first line contains an integer, N, the number of elements in arrays X and W.
The second line contains N space-separated integers that describe the elements of array X.
The third line contains N space-separated integers that describe the elements of array W.

Output Format
Print the weighted mean on a new line. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

Sample Input

STDIN           Function
-----           --------
5               X[] and W[] size n = 5
10 40 30 50 20  X = [10, 40, 30, 50, 20]  
1 2 3 4 5       W = [1, 2, 3, 4, 5]
Sample Output

32.0
"""

n = int(input())
numbers = list(map(int, input().split()))
weighted = list(map(int, input().split()))
sum_items = 0
for i in range(n):
    sum_items = sum_items + (numbers[i] * weighted[i])

print(round(sum_items/sum(weighted), 1))
