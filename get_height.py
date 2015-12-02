sample_dict = { 0:1,
                1:2,
                2:3,
                3:6,
                4:7,
                5:14,
                6:15,
                7:30,
                8:31,
                9:62,
               10:63  }


def get_height(cycles):
    if cycles in [0,1,2]: return cycles + 1
    
    height = 3
    for i in range(3, cycles+1, 2):
        height = height*2
        if cycles % 2 == 1 and i == cycles: 
            return height
        else:
            height = height+1
    return height
    
def get_height_bitwise(n):
    return ~(~1<<(n>>1)) << n%2

items=list(range(11))
for item in items:    
    print item, str(get_height_bitwise(item))