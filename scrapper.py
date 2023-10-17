from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_path = '/Users/ometelytsia/.bzt/selenium-taurus/tools/drivers/chromedriver/117.0.5938.92/chromedriver'
service = webdriver.ChromeService(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service)

driver.get('https://www.linkedin.com/')

INPUT = "names"

sleep(2)
driver.find_element(by=By.ID, value="session_key").send_keys("usr_name")
driver.find_element(by=By.ID, value="session_password").send_keys("pass")
# click_btn = "/html/body/main/section[1]/div/div/form/div[2]/button"
# driver.find_element(by=By.XPATH, value="click_btn").click()


def read_file(path):
    with open(path) as f:
        return f.readlines()


full_lines = read_file(INPUT)

for line in full_lines:
    name, country, region = line.split(",")
    if country == "India":
        country_code = '?geoUrn=%5B"102713980"%5D'
    elif country == "Australia":
        country_code = '?geoUrn=%5B"101452733"%5D'
    elif country == "United States":
        country_code = '?geoUrn=%5B"103644278"%5D'
    elif country == "Germany":
        country_code = '?geoUrn=%5B"101282230"%5D'
    elif country == "Spain":
        country_code = '?geoUrn=%5B"105646813"%5D'
    elif country == "Canada":
        country_code = '?geoUrn=%5B"101174742"%5D'
    elif country == "Austria":
        country_code = '?geoUrn=%5B"103883259"%5D'
    elif country == "Poland":
        country_code = '?geoUrn=%5B"105072130"%5D'
    else:
        exit(100)
    driver.get(f"https://www.linkedin.com/search/results/people/{country_code}&keywords={name}")
    sleep(5)
    count = 0
    try:
        count_str = driver.find_element(by=By.CLASS_NAME, value="search-results-container").find_element(by=By.XPATH, value="./child::*").text
        if len(count_str.split(" ")) == 2:
            count = int(count_str.split(" ")[0].replace(",", ""))
        elif len(count_str.split(" ")) == 3:
            count = int(count_str.split(" ")[1].replace(",", ""))
        else:
            raise Exception(f"Strange line: {count_str}")
        if count > 10:
            print(f"Too many results ({count}) found  for {name}")
        else:
            print(f"Review manually: {name}, count: {count}, county: {country}, region: {region}")
    except Exception as e:
        print(f"For {name} got: {e}")
    pass

driver.quit()