import time

from selenium import webdriver

driver = webdriver.Chrome()

sites = []
sitesDict = {}

with open("resources/lab2.txt") as f:
    for string in f.readlines():
        sites.append(string.replace("\n", ""))

sites.sort(key=len)
i = 1

for x in sites:
    driver.execute_script("window.open('" + x + "');")
    sitesDict[x] = driver.window_handles[i]
    i = i + 1
    time.sleep(0.5)

sites.sort()

for x in sites:
    print(sitesDict[x])

for x in sites:
    driver.switch_to.window(window_name=sitesDict[x])
    driver.close()

driver.quit()
