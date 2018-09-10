# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
# Do this in O(N) time

print("hello")


def maxsum(arr):
    max = arr[0]
    temp = 0
    for i in range(0, len(arr)+1):
        if i == len(arr)+1:
            if arr[i] > max:
                max = arr[i]
        else:
            for j in range(i+1, len(arr)+1):
                temp = sum(arr[i:j])
                if temp > max:
                    max = temp
                print(i, j, max)

    return print("Max Sum: ", max >= 0 and max or 0)


maxsum([34, -50, -42, -14, -5, -86])
