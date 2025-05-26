# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # === attach to existing Chrome debug session ===
# options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# driver_path = r"C:\Auto Programas\webdriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"
# driver = webdriver.Chrome(service=Service(driver_path), options=options)
# wait = WebDriverWait(driver, 10)

# # === (your add-to-cart logic runs prior to this) ===
# # [...] 

# # === now: navigate to Cart/Checkout page ===
# cart_url = (
#     "https://gfebs.am.mot-solutions.com/"
#     "OA_HTML/OA.jsp?"
#     "page=/oracle/apps/icx/icatalog/shopping/webui/NonCatalogRequestPG"
#     "&_ti=876005299&OAMC=77403_224_0&menu=Y"
#     "&oaMenuLevel=2&oapc=13&oas=L6moKsXtz_2IUcJgjn7Wjg..#"
# )
# driver.get(cart_url)

# # wait until at least one Update-Line icon is clickable
# wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[title='Update Line'], img[alt='Update Line']")))

# # grab all edit icons
# edit_icons = driver.find_elements(By.CSS_SELECTOR, "img[title='Update Line'], img[alt='Update Line']")

# for icon in edit_icons:
#     # wait for this specific icon to be clickable, scroll into view, then click
#     clickable = wait.until(EC.element_to_be_clickable((By.XPATH, f"//img[@title='Update Line' or @alt='Update Line'][@src='{icon.get_attribute('src')}']")))
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", clickable)
#     clickable.click()

#     # wait for the edit dialog
#     wait.until(EC.visibility_of_element_located((By.ID, "UpdateLineDialog")))

#     # 1) Update the account field
#     acct = driver.find_element(By.NAME, "MSIGL_Corp_Acct_Flex")
#     acct.clear()
#     acct.send_keys("140000-888353-BZ875-00-0000-000000-000-000000-000000")

#     # 2) Check the Urgent checkbox
#     urgent = driver.find_element(By.NAME, "Urgent")
#     if not urgent.is_selected():
#         urgent.click()

#     # 3) Set the Need-By Date
#     date_field = driver.find_element(By.NAME, "NeedByDate")
#     date_field.clear()
#     date_field.send_keys("01-Jun-2025 12:00:00")
#     date_field.send_keys(Keys.ENTER)

#     # 4) Save (Apply) changes
#     driver.find_element(By.XPATH, "//button[text()='Apply']").click()
#     wait.until(EC.invisibility_of_element_located((By.ID, "UpdateLineDialog")))

#     time.sleep(1)  # brief pause before next line

# # === finally, submit the entire request ===
# # driver.find_element(By.XPATH, "//button[text()='Submit']").click()