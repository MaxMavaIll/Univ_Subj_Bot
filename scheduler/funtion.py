import json, logging
import datetime, time
from os.path import abspath, exists

import config as cf


######################################### process time #######################################
def subject_time():
    data = cf.data["sub_times"]
    logging.debug(data[0])
    selected_time = data[0].split(":")
    # illya loh
    
    subj_time = datetime.timedelta(hours=int(selected_time[0]), minutes=int(selected_time[1]))

    return subj_time

def check_nearest_subject(now_time: datetime.timedelta):
    data = cf.data["sub_times"]
    while 1: 
        logging.debug(f"{data}")
        if data != []:
            subj_time = subject_time()
            rizn = subj_time - now_time
            if rizn < datetime.timedelta():
                
                logging.info(f"I delete {data[0]}")
                del data[0]
            else:
                break
        else:
            change_week()
            rizn = datetime.timedelta(minutes=21)
            break
    

    return rizn

def change_week():
    now = datetime.datetime.now()
    data = cf.data

    if data["sub_times"] == [] and now.weekday() == 6:
        data["week_one_two"] = (data["week_one_two"] + 1) % 2


def check_new_day():
    now_time = datetime.datetime.now()

    if ((now_time + datetime.timedelta( minutes = cf.time_repite )).day - now_time.day) == 1:
        cf.data["sub_times"] = cf.data_list

############################## Turn the number into sheet ##########################

def transfer_day_time_to_sheet() -> str:
    all_day = [ ["B","C","D","E","F","G"], ["J", "K", "L", "M", "N", "O"] ]

    data = cf.data
    subject_time = data["sub_times"][0]
    now = datetime.datetime.now()
    time_sheet = 27
    day_sheet = all_day[data["week_one_two"]][now.weekday()]
    
    for index in range(len(cf.data_list)):
        if subject_time == cf.data_list[index]:
            time_sheet += index
        
    return f"{day_sheet}{time_sheet}"

 