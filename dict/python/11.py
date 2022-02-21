# Write a Python program to implement the statistics functions (mean, median, mode) using statistics module.

import statistics

sd = [5,5,5,6,7,3,5,6,2,3,4]

print(f"Mode of the list of number {sd} is {statistics.mode(sd)}")
print(f"Median of the list of number {sd} is {statistics.median(sd)}")
print(f"Mean of the list of number {sd} is {statistics.mean(sd)}")

# Output
# Mode of the list of number [5, 5, 5, 6, 7, 3, 5, 6, 2, 3, 4] is 5
# Median of the list of number [5, 5, 5, 6, 7, 3, 5, 6, 2, 3, 4] is 5
# Mean of the list of number [5, 5, 5, 6, 7, 3, 5, 6, 2, 3, 4] is 4.636363636363637