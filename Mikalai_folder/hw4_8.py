# list1 = [1, 5, 2, 9, 2, 9, 1]
# for i in list1:
#     if list1.count(i) == 1:
#         print (i)




str = "After careful evaluation, in mid-2019 Boeing began changing the type of\
    automation in the assembly of the forward and aft fuselage sections from robots to flex \
    tracks. First developed by Boeing Commercial Airplanes, flex tracks are an automated \
    drilling technology proven effective on commercial programs such as the 787 Dreamliner \
    and defense programs as well as in the later stages of assembly of the 777. \
    Mechanics attach flexible tracks spanning the fuselage skin, then numerically \
    controlled drills ride along the tracks to drill holes while the mechanics manually attach\
    fasteners on the inside. The decision to change approaches, under FAA oversight, was driven \
    by experience that showed flex tracks deliver higher quality, requiring less work by hand\
    and with higher reliability, than what the robots had been capable of in the forward and\
    aft fuselage areas.".lower()

max_count = 0
max_char = ""

import string
for char in string.ascii_lowercase:
    #print(char,str.count(char))
    current_count = str.count(char)
    if current_count > max_count:
        #print(char, 'is current leader with ', current_count)
        max_count = current_count
        max_char = char
    else:
        pass
        #print('doing nothing')
print(max_char)
  
