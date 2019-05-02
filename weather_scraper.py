import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XMm__ZNKhQI")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id='seven-day-forecast')
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)
forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]
tomorrow = forecast_items[2]

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

img = tonight.find("img")
desc = img["title"]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# print(short_descs)
# # print(temps)
# # print(descs)

weather = pd.DataFrame({
    "period" : periods,
    "short_desc" : short_descs,
    "temp" : temps,
    "desc" : descs,
})

print(weather)
