"""
Make Bricks
We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks 
(5 inches each). Return True if it is possible to make the 
goal by choosing from the given bricks.
"""

def make_bricks(small, big, goal):
  
  
  return False

if __name__ == "__main__":  
    print make_bricks(3, 1, 8), "Expected: True"
    print make_bricks(3, 1, 9), "Expected: False"
    print make_bricks(3, 2, 10), "Expected: True"
    print make_bricks(3, 2, 8), "Expected: True" 
    print make_bricks(3, 2, 9), "Expected: False" 
    print make_bricks(6, 1, 11), "Expected: True"
    print make_bricks(6, 0, 11), "Expected: False"
    print make_bricks(1, 4, 11), "Expected: True"
    print make_bricks(0, 3, 10), "Expected: True"
    print make_bricks(1, 4, 12), "Expected: False"
    print make_bricks(3, 1, 7), "Expected: True" 
    print make_bricks(1, 1, 7), "Expected: False"  
    print make_bricks(2, 1, 7), "Expected: True" 
    print make_bricks(7, 1, 11), "Expected: True"
    print make_bricks(7, 1, 8), "Expected: True" 
    print make_bricks(7, 1, 13), "Expected: False"
    print make_bricks(43, 1, 46), "Expected: True"
    print make_bricks(40, 1, 46), "Expected: False"
    print make_bricks(40, 2, 47), "Expected: True"
    print make_bricks(40, 2, 50), "Expected: True"
    print make_bricks(40, 2, 52), "Expected: False"
    print make_bricks(22, 2, 33), "Expected: False"
    print make_bricks(0, 2, 10), "Expected: True" 
    print make_bricks(1000000, 1000, 1000100), "Expected: True" 
    print make_bricks(2, 1000000, 100003), "Expected: False"
    print make_bricks(20, 0, 19), "Expected: True" 
    print make_bricks(20, 0, 21), "Expected: False"
    print make_bricks(20, 4, 51), "Expected: False"
    print make_bricks(20, 4, 39), "Expected: True" 