"""Scraper Builder
Version: 1.0.0
Author: BIMA

Scraper builder is a builder to generate script code automatically after config some settings.
Scraper builder using XPATH as a selector.
"""
import json
from collections import defaultdict
import time
import random

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Setting the driver
chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# ============================ Generated by API ==================================== #
# page_xpath is a selector for pagination. If the selector using endpoint, just put the endpoint with python placeholder
# Example: page_xpath = "https://www.99.co/id/jual/rumah?hlmn={}"
page_xpath = ""

# initial_element is a selector for benchmarking. If the element exists, scraper will assume that the page has
# successfully loaded
# Example: initial_element = "//h1[contains(@class, 'search-title__keyword')]"
reference_element = ""

# list_of_details_url is a selector that will take all detail url to take the data later by the scraper
# Example: list_of_details_url = "//div[contains(@class, 'superfeatured')]/div[2]/div/div/div[2]/div/h2/a"
list_of_details_url = ""

# max_page is a variable that contains how many pages that will be scraped by the scraper
# Example: max_page = 2
max_page = 2

# filename is a selector that will take all detail url to take the data later by the scraper
# Example: list_of_details_url = "scraper1.json"
filename = ""

# Initialize the driver
driver = Chrome(options=chrome_options)

# Base URL or homepage
# This URL should show the list url
# base_url = "https://www.99.co/id/jual/rumah?hlmn=1"
base_url = ""

# Go to the web and wait until the reference element exists
driver.get(base_url)
_ = WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.XPATH, reference_element)))


# Every element that want to be scraped by the scraper
# Total number of elements depends on user input when set up configuration
# Example:
# image_element = "//div[contains(@class, 'galery-component__wrapper')]/img"
# price_element = "//div[contains(@class, 'property-secondary-heading__price')]/h2"
# installment_element = "//p[contains(@class, 'property-secondary-heading__installment')]/a"
# title_element = "//h1[contains(@class, 'property-secondary-heading__title')]"
# feature_element = "//ul[contains(@class, 'property-secondary-heading__feature')]"
# detail_property = "//div[contains(@class, 'property-secondary-vl__detail__column')]"
# facility_element = "//div[contains(@class, 'property-secondary__facilities__value')]"
# location_element = "//div[contains(@class, 'r123-listing-summary-v2__address')]"

image_element = ""
price_element = ""
installment_element = ""
title_element = ""
feature_element = ""
detail_property = ""
facility_element = ""
location_element = ""

pages = defaultdict(list)


def open_new_tab(url: str):
    driver.switch_to.new_window()
    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)
    return driver.get(url)


i = 1
while i <= max_page:
    list_of_details = [e.get_attribute("href") for e in driver.find_elements(By.XPATH, list_of_details_url)]

    for h in list_of_details:
        open_new_tab(url=h)
        data = {}
        # ========================= Generated by API =============================== #
        try:
            image = [e.get_attribute("src") for e in driver.find_elements(By.XPATH, image_element)]
        except NoSuchElementException as e:
            image = "no image"
        try:
            price = driver.find_element(By.XPATH, price_element).text
        except NoSuchElementException as e:
            price = "no price"
        try:
            installment = driver.find_element(By.XPATH, installment_element).text
        except NoSuchElementException as e:
            installment = "no cicilan"
        try:
            feature = [e.text for e in driver.find_elements(By.XPATH, feature_element)]
        except NoSuchElementException as e:
            feature = "no feature"
        try:
            detail_prop = [e.text for e in driver.find_elements(By.XPATH, detail_property)]
        except NoSuchElementException as e:
            detail_prop = "no detail prop"
        try:
            title = driver.find_element(By.XPATH, title_element).text
        except NoSuchElementException as e:
            title = "no title"
        try:
            facility = driver.find_element(By.XPATH, facility_element).text
        except NoSuchElementException as e:
            facility = "no facility"
        try:
            loc = driver.find_element(By.XPATH, location_element).text
        except NoSuchElementException:
            loc = "no loc"

        data["image"] = image
        data["price"] = price
        data["installment"] = installment
        data["title"] = title
        data["feature"] = feature
        data["detail_property"] = detail_prop
        data["facility"] = facility
        data["loc"] = loc
        # ========================= Generated by API =============================== #

        pages[f"page{i}"].append(data)

        time.sleep(random.random() * 5)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.close()
        driver.switch_to.window(windows[0])
        time.sleep(random.random() * 2)

    i += 1
    if "https" not in page_xpath and driver.find_element(By.XPATH, page_xpath):
        driver.find_element(By.XPATH, page_xpath).click()
    else:
        driver.get(page_xpath.format(i))
        _ = WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.XPATH, reference_element)))
    time.sleep(2)

# Save to JSON
with open(filename, "w") as f:
    json.dump(pages, f)

driver.close()