"""This prog will add hours succesively
1st successful code coded on 25 Feb 12 0635"""

import math

def hr2min(hour):
    x = hour.split(':')
    minutes = int(x[0]) * 60 + int(x[1])
    return minutes

def min2hr(minutes):
    hr = math.floor(minutes/60)
    mn = minutes % 60
    return (str(hr) + ':' + str(mn))

print("""
===================================
Welcome to Hour Calculator
by: Touhidur Rahman
http://about.me/tanimkg

Enter Hour in this format >> hh:mm
Example >> 8:45

Type 'ok' to stop calculation
Type 'reset' to restart calculation
===================================
""")

minutes = 0
while True:
    add = input("Hour >>  ")
    if add == 'ok':
        break
    elif add == 'reset':
        minutes = 0
        continue
    elif ':' not in add:
        print('Wrong Entry! Format <<hh:mm>> Type \'ok\' to quit and \'reset\' to start again.')
        pass
    else:
        minutes += int(hr2min(add))
        print('Total >> ' + min2hr(minutes))



    
        

