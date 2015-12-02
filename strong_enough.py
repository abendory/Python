import unittest
import math 

def strong_enough( earthquake, age ):
    mag=1
    total=0
    building_value = 1000*math.e**(-.01*age)
    for shockwave in earthquake:
        for tremor in shockwave:
            total += tremor
        mag *= total
        total = 0
    return "Safe!" if mag < building_value else "Needs Reinforcement!"

assert strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2), "Safe!"
assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 2), "Safe!"
assert strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3), "Needs Reinforcement!"
