# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # === Load data ===
# column_names = ["Manufacturer Part Number", "Digi-Key Part Number", "Description", "Quantity", "Unit Price"]
# df = pd.read_csv("sample csv - Sheet1.csv", header=None, names=column_names, skiprows=1)
# # df = pd.read_csv("sample csv - Sheet1.csv", skiprows=1)  # skip DigiKey header
# print("Columns found", df.columns.tolist())
# df.columns = [col.strip() for col in df.columns]  # clean column names

# # === Set up Selenium ===
# options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # assumes Chrome was launched in debug mode

# driver_path = "C:\\Auto Programas\\webdriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
# driver = webdriver.Chrome(service=Service(driver_path), options=options)

# # === Loop through each row ===
# for index, row in df.iterrows():
#     quantity = str(row["Quantity"])
#     description = row["Description"]
#     part_num = row["Digi-Key Part Number"]
#     price = str(row["Unit Price"])

#     # Format description
#     full_desc = f'{quantity} pcs of {description} on REEL/ Part #: {part_num}'

#     print(f"\nFilling item {index+1}:\n{full_desc}")

#     # === Fill fields ===
#     # Item Description
#     desc_field = driver.find_element(By.NAME, "ItemDescription")
#     desc_field.clear()
#     desc_field.send_keys(full_desc)

#     # Quantity
#     qty_field = driver.find_element(By.NAME, "Quantity")
#     qty_field.clear()
#     qty_field.send_keys(quantity)

#     # Unit Price
#     price_field = driver.find_element(By.NAME, "UnitPrice")
#     price_field.clear()
#     price_field.send_keys(price)

#     # === Manual confirmation ===
#     input("Review this item, then press Enter to continue...")

#     # === Click Add to Cart ===
#     add_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
#     add_btn.click()

#     print("Submitted. Waiting 5 seconds for page refresh...")
#     time.sleep(5)
# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # === Load CSV data ===
# column_names = ["Manufacturer Part Number", "Digi-Key Part Number", "Description", "Quantity", "Unit Price"]
# df = pd.read_csv("sample csv - Sheet1.csv", header=None, names=column_names, skiprows=1)
# print("Columns found:", df.columns.tolist())
# df.columns = [col.strip() for col in df.columns]

# # === Set up Selenium ===
# driver_path = r"C:\Auto Programas\webdriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# service = Service(driver_path)
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 10)

# # === Navigate to procurement page and wait for manual login ===
# driver.get("https://gfebs.am.mot-solutions.com/OA_HTML/OA.jsp?page=/oracle/apps/icx/icatalog/shopping/webui/NonCatalogRequestPG")
# input("Please log in manually and load the Non-Catalog Request page. Then press Enter here to continue...")

# # === Loop through each item and autofill ===
# for index, row in df.iterrows():
#     quantity = str(row["Quantity"])
#     description = row["Description"]
#     part_num = row["Digi-Key Part Number"]
#     price = str(row["Unit Price"])

# full_desc = f'{quantity} pcs of {description} on REEL/ Part #: {part_num}'
# print(f"\nFilling item {index+1}:\n{full_desc}")

# # Fill Description
# desc_field = wait.until(EC.presence_of_element_located((By.NAME, "ItemDescription")))
# desc_field.clear()
# desc_field.send_keys(full_desc)

# # Fill Quantity
# qty_field = driver.find_element(By.NAME, "Quantity")
# qty_field.clear()
# qty_field.send_keys(quantity)

# # Fill Unit Price
# price_field = driver.find_element(By.NAME, "UnitPrice")
# price_field.clear()
# price_field.send_keys(price)

# # Wait for manual confirmation
# input("Review this item, then press Enter to continue...")

# # Click Add to Cart
# add_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
# add_btn.click()

# print("Submitted. Waiting 5 seconds for page refresh...")
# time.sleep(5)


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Load CSV data ===
column_names = ["Part Number","Description", "Quantity", "Unit Price"]
df = pd.read_csv("Quote Auto.csv", header=None, names=column_names, skiprows=1)
print("Columns found:", df.columns.tolist())
df.columns = [col.strip() for col in df.columns]

# === Set up Selenium with stealth mode ===
driver_path = "C:\Auto Programas\webdriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=service, options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

wait = WebDriverWait(driver, 10)

# === Open Chrome and wait for manual navigation/login ===
driver.get("https://google.com") # just opens Chrome — you navigate to procurement page manually
input("Please log in and open the procurement form. Then press Enter here to start autofill...")

# === Loop through each item ===
for index, row in df.iterrows():
    quantity = str(row["Quantity"])
    description = row["Description"]
    part_num = row["Part Number"]
    price = str(row["Unit Price"])

    full_desc = f'{quantity} pcs of {description} on REEL/ Part #: {part_num}'
    print(f"\nFilling item {index+1}:\n{full_desc}")

    desc_field = wait.until(EC.presence_of_element_located((By.NAME, "ItemDescription")))
    desc_field.clear()
    desc_field.send_keys(full_desc)

    qty_field = driver.find_element(By.NAME, "Quantity")
    qty_field.clear()
    qty_field.send_keys(quantity)

    price_field = driver.find_element(By.NAME, "UnitPrice")
    price_field.clear()
    price_field.send_keys(price)

    input("Review this item, then press Enter to continue...")

    add_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
    add_btn.click()

    print("Submitted. Waiting 3 seconds for page refresh...")
    time.sleep(3)



