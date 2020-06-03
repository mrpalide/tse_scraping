import time

import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver

link = "http://www.tsetmc.com/Loader.aspx?ParTree=15131F"

df_column = [
    "namad",
    "nam",
    "tedad",
    "hajm",
    "arzesh",
    "dirooz",
    "avalin",
    "akharin-meghdar",
    "akharin-taghir",
    "akharin-darasd",
    "payani-meghdar",
    "payani-taghir",
    "payani-darasd",
    "kamtarin",
    "bishtarin",
    "eps",
    "p/e",
    "kharid-tedad",
    "kharid-hajm",
    "kharid-gheymat",
    "sell-gheymat",
    "sell-hajm",
    "sell-tadad",
]


def get_data():
    data_df = pd.DataFrame(columns=df_column)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.binary_location = "/usr/bin/google-chrome-stable"
    chrome_driver_path = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
    driver.get(link)
    time.sleep(10)
    page_source = driver.page_source
    soup_data = bs(page_source, "html.parser")
    html_data = soup_data.findAll("div", {"class": "{c}"})
    for i in html_data:
        i_data = i.findAll("div")
        t = 0
        tmp_array = []
        for j in i_data:
            if t not in [4, 19, 23]:
                tmp_array.append(j.text)
            t += 1
        data_df = data_df.append(
            pd.Series(tmp_array, index=data_df.columns), ignore_index=True
        )
    data_df.to_csv(
        f'data_{time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())}.csv',
        index=False,
        header=True,
    )


if __name__ == "__main__":
    get_data()
