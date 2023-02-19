import json, os
import logging, asyncio
import config as cf
from datetime import datetime, timedelta

from aiogram import Bot
from tgbot.config import load_config
# from aiogram.dispatcher.fsm.storage.redis import RedisStorage

from scheduler import funtion as f # new_registri_time, create_dict, check_existing_file, add_last_update_time, delete_previous_hour
from GoogleSheet import function as gsf

path_save_file = "data/pack_for_send.json"
time_del_message = 60 * 60

#from schedulers.exceptions import raise_error

async def add_user_checker(bot: Bot):
    logging.info("start add_user_checker")
    if cf.data["sub_times"] != []:
        now_time = datetime.now()
        now_time = timedelta(hours=now_time.hour, minutes=now_time.minute)

        if f.check_nearest_subject(now_time) <= timedelta(minutes=20):
            logging.info(f"now_time {now_time}\ndata {cf.data}")
            
            sheet_DayTime = f.transfer_day_time_to_sheet()
            logging.info(sheet_DayTime)
            data_subj = gsf.get_value(sheet_DayTime)
            env = load_config(".env")
            
            await bot.send_message(env.tg_bot.group_chat, f"{data_subj[0]}")
            await bot.send_message(env.tg_bot.group_chat, f"{data_subj[1]}")

    else:
        f.check_new_day()
        logging.info(f"Stady is finish. Data {cf.data}")

    # await bot.send_message(id, f"Хтось записався на <b></b>")
    
