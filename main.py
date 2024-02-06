from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def buying():
    print("new buying cycle")

    # converting store data into price dic
    store_data = driver.find_element(By.ID, value="store").text
    store_data = store_data.split("." and "\n")
    for data in store_data:  # count number gets removed
        if len(data) <= 4:
            store_data.remove(data)
    buy_data = []
    for index in range(0, len(store_data), 2):
        buy_data.append(store_data[index].split(" - "))
    prices = {buy_data[i][0]: buy_data[i][1].replace(",", "") for i in range(0, len(buy_data))}

    highest_item = ""
    for item in prices:
        if int(prices[item]) <= int(driver.find_element(By.ID, value="money").text.replace(",", "")):
            highest_item = item
            print(f"new highest item: {highest_item}")
    prices.clear()
    buy_data.clear()
    print(f"bought {highest_item}")
    highest_item_frame = driver.find_element(By.ID, value=f"buy{highest_item}")
    highest_item_frame.click()


start_time_buying = time.time()
start_time_playing = time.time()
cookie = driver.find_element(By.ID, value="cookie")
while True:
    cookie.click()
    elapsed_time_buying = time.time() - start_time_buying
    elapsed_time_playing = time.time() - start_time_playing

    if elapsed_time_buying >= 5:
        start_time_buying = time.time()
        buying()

    if elapsed_time_playing >= 300:
        print(driver.find_element(By.ID, value="cps").text)
        driver.quit()
        break
