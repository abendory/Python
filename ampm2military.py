import re

n = '12:59:34AM' #list(raw_input().split(':'))
print n
n = n.split(':')
items = re.split("([a-zA-Z]+)", n[2])  
mil_t = []
if items[1] == 'PM' and n[0] != '12': 
    mil_t.append(int(n[0])+12)
elif items[1] == 'AM' and n[0] == '12':
	mil_t.append(0)
else:
    mil_t.append(int(n[0]))
mil_t.append(int(n[1]))
mil_t.append(int(items[0]))
time_array = []
for i in range(3):
    if mil_t[i] < 10:
        time_array.append('0'+str(mil_t[i]))
    else:
        time_array.append(str(mil_t[i]))
        
print time_array[0] + ':' + time_array[1] + ':' + time_array[2]

