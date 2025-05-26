import time
import pandas as pd
import selenium import webdriver
from selenium.webdriver.common by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load CSV data (purchase order from excel or pdf format)
#skip first row (skip header)
column_names = ["Part Number", "Description", "Quantity", "Unit Price"]
df = pd.read_csv("Quote Auto.csv", header = None, names = column_names, skiprows=1)
#ensure column names found
print("Coloumn names:", df.columns.tolist())
for col in df.columns:
    df.columns = col.strip() #gets rid of any formatting

#set up selenium in stealth mode
driver_path = "C:\Auto Programas\webdriver\chromedriver-win64\chromedriver-win64\chromedriver.exe" #path to chrome webdriver
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


#open up google
driver.get("https//google.com")
input("Please log in and proceed to procurement form, then press enter to continue")

#Find input field, clear wtv is there, and write from csv file
for index, row in df.iterrows():
    description = rows["Description"]
    quantity = str(rows["Quantity"])
    price = str(rows["Price"])
    part_num = rows["Part Number"]

    full_desc = f"{quantity} pcs of {description} on REEL / #Part Number: {part_num}"
    desc_field  = wait.until(EC.presence_of_element_located(By.Name,"ItemDescription"))
    desc_field.clear()
    desc_file.sendkeys(full_desc)
    
    qty_field = wait.until(EC.presence_of_element_located(By.Name, "Quantity"))
    qty_field.clear()
    qty_field.sendkeys(quantity)

    price_field = wait.until(EC.presence_of_element_located(By.Name, "UnitPrice"))
    price_field.clear()
    price_field.sendkeys(price)
    input("Review if everything looks ok! Press Enter to continue...")
    add_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
    add_btn.click()
    
    print("Submitted.Wait 3s for page to refresh...")
    time.sleep(3)





