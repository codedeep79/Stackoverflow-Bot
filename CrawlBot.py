from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from console_logging.console import Console
import json
import os, re

console = Console()
curated_lists = []
browser = webdriver.Chrome()
console.info("Initialized Chrome Webdriver.")

def get_repos(pages=100):
    console.log("Now entering signup process.")
    # Get repos
    console.info("Loaded search results.")
    for page in range(pages):
        browser.get(
        'https://stackoverflow.com/tags?page=%d&tab=popular' %page)
        search_results = browser.find_elements_by_class_name('grid-layout--cell')
        console.info("Found %d results..." % len(search_results))
        sleep(1)
        for search_result in search_results:
            try:
                # Get text content in repo-list-item class by innerText JS attribute
                resultText = search_result.get_attribute('innerText').split('\n')
                tagName = repr(resultText[0].encode('ascii', 'ignore'))
                tagNameList =  list(tagName)
                tagNameList =  tagNameList[1 : len(tagNameList) - 1]
                tagName = ''.join(str(tag) for tag in tagNameList)
                tagNameList = re.findall("\D|[\D\d]\D", tagName)
                tagName = ''.join(str(tag) for tag in tagNameList)
                #tagName = ''.join([_str for _str in tagName if not _str.isdigit()]).title()

                descriptionTag = repr(resultText[1].encode('ascii', 'ignore')).title()
                descriptionTagList =  list(descriptionTag)
                descriptionTagList =  descriptionTagList[1 : len(descriptionTagList) - 1]
                descriptionTag = ''.join(str(description) for description in descriptionTagList)
                curated_lists.append({
                    'tagName': tagName,
                    'descriptionTag': descriptionTag
                })
                console.success("Added " + tagName)
            except Exception as e:
                console.error(str(e))
        sleep(2)

try:
    get_repos(pages=1619)
except:
    pass

with open('./README.json', 'w') as curated_list_json_file:
    json.dump(curated_lists, curated_list_json_file, indent=4)
