import requests
from bs4 import BeautifulSoup

base = "https://dilbert-viewer.herokuapp.com"

url = "/1989-04-16" # The first Dilbert comic
data = []

while True:
    response = requests.get(base + url)
    soup = BeautifulSoup(response.content, "html.parser")

    currentData = {
        "date": "",
        "img_src": ""
    }

    # extract the date from the current page
    date_tag = soup.find("h1")
    if date_tag:
        date = date_tag.text
        currentData["date"] = date
        print(date, end=" ")

    # Extract the img src from the current page
    img_tag = soup.find("img")
    if img_tag:
        img_src = img_tag["src"]
        currentData["img_src"] = img_src
        print(img_src)

    data.append(currentData)

    # Find the next page link
    next_link = soup.find("a", id="next-button")
    if next_link and next_link["href"] != url:
        url = next_link["href"]
    else:
        break

    # listen for a keypress, and dump the file in case there's one
    import msvcrt
    if msvcrt.kbhit():
        if msvcrt.getch() == b"q":
            break

# dump the data to a json file
import json
with open("data.json", "w") as f:
    json.dump(data, f)
