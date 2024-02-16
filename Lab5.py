# Name: Berfredd Quezon
# Section: 11

from data import *
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.

# Part 3
''' Design Recipe
input: two time objects
output: one time object
purpose: add two times together and return the added time
Steps:
1. create a new time object new_time and give its hour, minute, and seconds attributes a value of 0
2. change the new_time seconds to the sum of the inputted time objects
3. check if the new_time seconds value is greater than or equal to 60
    3.1 if it is, add 1 to the value of the new_time minutes
    3.2 subtract 60 from the current value of new_time seconds
4. add the sum of the two time objects minute values to the current minute value
5. check if the new_time minute value is greater than or equal to 60
    5.1 if it is, add 1 to the value of the new_time hours
    5.2 subtract 60 from the current new_time minutes value
6. set the new_time hours value to the sum of the hours attributes of the two time objects
7. return new_time
'''
def time_add(time1:Time, time2:Time) -> Time:
    new_time = Time(0,0,0)
    new_time.second = time1.second + time2.second
    if new_time.second >= 60:
        new_time.minute += 1
        new_time.second -= 60
    new_time.minute += time1.minute + time2.minute
    if new_time.minute >= 60:
        new_time.hour += 1
        new_time.minute -= 60
    new_time.hour += time1.hour + time2.hour
    return new_time

# Part 4
''' Design Recipe
input: list of floats
output: bool
purpose: return True or False if inputted list is in descending order
Steps:
1. check if the list is empty
    1.1 if true, return False
2. create a variable count and set it equal to 1
3. loop through each index in the list
    3.1 check if the value of the current index being evaluated is greater than the value of the next index
        3.1.1 if true, add 1 to the count variable
4. check if the count variable is equal to the length of the list
    4.1 if it is, return True
    4.2 if it isn't, return False
'''
def is_descending(lst:list[float]) -> bool:
    if not lst:
        return False
    count = 1
    for val in range(len(lst)-1):
        if lst[val] > lst[val+1]:
            count += 1
    if count == len(lst):
        return True
    else:
        return False

# Part 5
''' Design Receipe
input: list of integers, integer, and integer
output: integer
purpose: return the largest value in an inputted list between an inputted range of values
Steps:
1. check if list is empty
    1.1 if it is return None
2. check if lower is greater than upper
    2.1 if it is return None
3. check if the upper index is greater than or equal to the length of the list
    3.1 if true return -1
4. create variable large to store the largest value and set it equal to the value in the list with the index lowest
5. loop through each index in the list in range of lower and upper plus 1
    5.1 check if the variable large is less than the next value in the list
        5.1.1 if true set large equal to that value in the list
6. return large
'''
def largest_between(lst:list[int], lower:int, upper:int) -> Optional[int]:
    if not lst:
        return None
    if lower > upper:
        return None
    if upper >= len(lst):
        return -1
    large = lst[lower]
    for val in range(lower, upper+1):
        if large < lst[val]:
            large = lst[val]
    return large

# Part 6
''' Design Receipe
input: list of point objects
output: integer
purpose: return the index of the point with the greatest distance from the origin from a list of points
Steps:
1. check if list is empty
    1.1 return None if true
2. create a list named dist to store a list of the distances from the origin of each point
3. create a variable large to store the largest value in the list dist 
4. create a variable idx to store the index of the greatest value in the list and set it equal to 0
5. loop through each index in the length of the list dist
    5.1 check if large is equal to the value at the index
        5.1.1 if it is, set idx equal to that index
6. return idx
'''
'''
input: two point objects
output: an int
purpose: return the euclidean distance (square root of the difference of the points squared) between two points
steps:
1. create variable to store answer
2. find the euclidean distance between the points
3. return answer
'''
def euclidean_distance(P1:Point,P2:Point) -> int:
    answer = round(math.sqrt(math.pow(P1.x-P2.x,2)+math.pow(P1.y-P2.y,2)))
    return answer

'''
input: list of Point objects
output: list of integers
purpose: create a list that has the distance from the origin from an original list of points
steps:
1. check if list is empty -> return None if true
2. create an empty list distance
3. loop through each value in the list
    3.1 add the euclidean distance of each point from the origin to the list distance
4. return answer
'''
def distance_from_origin(lst:list[Point]) -> Optional[list[int]]:
    if not lst:
        return None
    distance = []
    for val in lst:
        distance.append(euclidean_distance(val,Point(0,0)))
    return distance

def furthest_from_origin(lst:list[Point]) -> Optional[int]:
    if not lst:
        return None
    dist = distance_from_origin(lst)
    large = largest_between(dist,0,len(lst)-1)
    idx = 0
    for val in range(len(dist)):
        if large == dist[val]:
            idx = val
    return idx



