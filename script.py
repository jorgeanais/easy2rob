from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
data = dict()

for number in range(520000, 530000):
    codigo = f"SYGH00{number}"
    driver.get(f"https://cloud-deliveryservices.cl/item/PagarImpuesto/{codigo}")

    try:
        form = driver.find_element(By.XPATH, "//input[@value='Ir a pagar'][@type='submit']")
        form.click()

        time.sleep(1)

        h5 = driver.find_element(By.XPATH, "//html/body/app-root/app-home/main-panel/main/section/left-panel/div/app-comerce-detail/div/div[2]/h5")
        texto = h5.text
        print(codigo, texto)
        data[codigo] = texto
        
    except:
        print(f"An exception occurred: {codigo}")
        
   

driver.close()

df = pd.DataFrame.from_dict(data, orient='index')
df.to_csv("output.csv")
