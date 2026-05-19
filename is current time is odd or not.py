from datetime import datetime

odd = [1,3,5,7,9,11,12,13,15,17,19,21,23,25,2,7,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
right_this_minute = datetime.today().minute
if right_this_minute in odd:
    print("this minute seems a littel odd")
else:
    print("not odd minute")