
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import builtins
from time import sleep




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Define floors

floors = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7
          ]

# max_weight = 50
# lift_weight = 0

default_floor = floors[0]
print('Lift at floor 0')


#Handle elevator request

elevator_request = int(input("Enter floor number(1-7)"))

if elevator_request==floors[7] and default_floor:
    print(elevator_request)
    sleep(35)
    floor = floors[0]
elif elevator_request==floors[6] and default_floor:
    print(elevator_request)
    sleep(30)
    floor = floors[0]
elif elevator_request == floors[5] and default_floor:
    print(elevator_request)
    sleep(25)
    floor = floors[0]
elif elevator_request == floors[4] and default_floor:
    print(elevator_request)
    sleep(20)
    floor = floors[0]
elif elevator_request == floors[3] and default_floor:
    print(elevator_request)
    sleep(15)
    floor = floors[0]
elif elevator_request == floors[2] and default_floor:
    print(elevator_request)
    sleep(10)
    floor = floors[0]
elif elevator_request == floors[1] and default_floor:
    print(elevator_request)
    sleep(5)
    floor = floors[0]
else:
    sleep(0)
    floor = floors[0]

if elevator_request==floors[7] and floors[1]:
    print(elevator_request)
    sleep(30)
    floor = floors[1]
elif elevator_request==floors[6] and floors[1]:
    print(elevator_request)
    sleep(25)
    floor = floors[1]
elif elevator_request == floors[5] and floors[1]:
    print(elevator_request)
    sleep(20)
    floor = floors[1]
elif elevator_request == floors[4] and floors[1]:
    print(elevator_request)
    sleep(15)
    floor = floors[1]
elif elevator_request == floors[3] and floors[1]:
    print(elevator_request)
    sleep(10)
    floor = floors[1]
elif elevator_request == floors[2] and floors[1]:
    print(elevator_request)
    sleep(5)
    floor = floors[1]
elif elevator_request==floors[7] and floors[2]:
    sleep(25)
    floor = floors[2]
elif elevator_request==floors[6] and floors[2]:
    sleep(20)
    floor = floors[2]
elif elevator_request == floors[5] and floors[2]:
    sleep(15)
    floor = floors[2]
elif elevator_request == floors[4] and floors[2]:
    sleep(10)
    floor = floors[2]
elif elevator_request == floors[3] and floors[2]:
    sleep(5)
    floor = floors[2]
elif elevator_request == floors[1] and floors[2]:
    sleep(5)
    floor = floors[2]
elif elevator_request == floors[0] and floors[2]:
    sleep(10)
    floor = floors[2]

elif elevator_request==floors[7] and floors[3]:
    sleep(20)
    floor = floors[3]
elif elevator_request==floors[6] and floors[3]:
    sleep(15)
    floor = floors[3]
elif elevator_request == floors[5] and floors[3]:
    sleep(10)
    floor = floors[3]
elif elevator_request == floors[4] and floors[3]:
    sleep(5)
    floor = floors[3]
elif elevator_request == floors[3] and floors[3]:
    sleep(5)
    floor = floors[3]
elif elevator_request == floors[2] and floors[3]:
    sleep(5)
    floor = floors[3]
elif elevator_request == floors[1] and floors[3]:
    sleep(10)
    floor = floors[3]

elif elevator_request==floors[7] and floors[4]:
    sleep(15)
    floor = floors[4]
elif elevator_request==floors[6] and floors[4]:
    sleep(10)
    floor = floors[4]
elif elevator_request == floors[5] and floors[4]:
    sleep(5)
    floor = floors[4]
elif elevator_request == floors[3] and floors[4]:
    sleep(5)
    floor = floors[4]
elif elevator_request == floors[2] and floors[4]:
    sleep(10)
    floor = floors[4]
elif elevator_request == floors[1] and floors[4]:
    sleep(15)
    floor = floors[4]
elif elevator_request==floors[7] and floors[5]:
    sleep(10)
    floor = floors[5]
elif elevator_request==floors[6] and floors[5]:
    sleep(5)
    floor = floors[5]
elif elevator_request == floors[4] and floors[5]:
    sleep(5)
    floor = floors[5]
elif elevator_request == floors[3] and floors[5]:
    sleep(10)
    floor = floors[5]
elif elevator_request == floors[2] and floors[5]:
    sleep(15)
    floor = floors[5]
elif elevator_request == floors[1] and floors[5]:
    sleep(20)
    floor = floors[5]
elif elevator_request==floors[7] and floors[6]:
    sleep(5)
    floor = floors[6]
elif elevator_request==floors[5] and floors[6]:
    sleep(5)
    floor = floors[6]
elif elevator_request == floors[4] and floors[6]:
    sleep(10)
    floor = floors[6]
elif elevator_request == floors[3] and floors[6]:
    sleep(15)
    floor = floors[6]
elif elevator_request == floors[2] and floors[6]:
    sleep(20)
    floor = floors[6]
elif elevator_request == floors[1] and floors[6]:
    sleep(25)
    floor = floors[6]
elif elevator_request==floors[7] and floors[7]:
    sleep(5)
    floor = floors[7]
elif elevator_request==floors[5] and floors[7]:
    sleep(5)
    floor = floors[7]
elif elevator_request == floors[4] and floors[7]:
    sleep(10)
    floor = floors[7]
elif elevator_request == floors[3] and floors[7]:
    sleep(15)
    floor = floors[7]
elif elevator_request == floors[2] and floors[7]:
    sleep(20)
elif elevator_request == floors[1] and floors[6]:
    sleep(25)
    floor = floors[6]
else:
    sleep(0)
    floor = floors[6]

# Define time taken in every floor
for floor in floors:
    print(floor)
    # if max_weight > lift_weight:
    #     print('weight overload, reduce weight by exiting')
    #     sleep(10)
    #     print('slept for 10 seconds')
    # else:
    #     continue




