import requests as rq
import gspread, logging


gc = gspread.service_account()

def get_value(raw_col: str = "B27") -> list:
    wks = gc.open("Univ").sheet1
    data = wks.get(f"{raw_col}")[0][0].split(", ")

    logging.info(data)
    return data
















# user =  {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
# url = "https://vo.uu.edu.ua/login/index.php"
# # "illya2033", "Halloillya"
# data = rq.post(url, headers=user, data={"username": "Hallo", "password": "Halloillya"})

# with open("GoogleSheet/write.html", "w") as file:
#     file.write(data.text)