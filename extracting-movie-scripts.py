import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import shutil
import os

def getScript(url):
    page = BeautifulSoup(requests.get(url).content,"html.parser")
    page_results = page.find_all("a")
    for pr in range(len(page_results)):
        if "Read" in str(page_results[pr]):
            script_url = page_results[pr]["href"]
            script_page_content = requests.get("https://imsdb.com"+script_url)
            if script_page_content.status_code==200:
                script_page = BeautifulSoup(script_page_content.content,"html.parser")
                if script_page.find("pre"):
                    story = script_page.find("pre").get_text()
                    story = ' '.join(story.split())
                    re.findall('\w+',story)
                    return story
                else:
                    return None  
                
def getMovieList(results):
    for p in range(len(results)):
        item = results[p]
        movie = item.find("a")["href"]
        if 'Movie Scripts' in movie:
            url = "https://imsdb.com"+movie
            title = re.split("/",movie)[2].replace(" Script","").replace(" ","-")
            print("Getting the script for",title)
            script = getScript(url)
            script_path = path+"movie_scripts"
            if script is not None:
                if not os.path.isdir(script_path):
                    os.makedirs(script_path)
                with open(script_path+"\\"+title+'.txt', 'wb') as file:
                    file.write(bytes(script,'utf-8'))
                print("Successfully extracted",title)

path = 'YOUR PATH'
url = "https://imsdb.com/genre/Romance"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("p")
getMovieList(results)