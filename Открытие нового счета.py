from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/.../.../chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1920,1080)
driver.find_element(By.XPATH, "//*[@id='login-button']").click()
driver.find_element(By.XPATH, "//*[@id='login-otp-button']").click()
driver.find_element(By.ID, "bank-overview").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='overview-accounts-container']/h2/span[1]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='contentbar']/form/div/a").click()
time.sleep(2)
driver.find_element(By.ID, "currencySelect").click()
driver.find_element(By.XPATH, "//*[@id='currencySelect']/option[3]").click()
driver.find_element(By.ID, "account-branch").click()
driver.find_element(By.XPATH, "//*[@id='account-branch']/option[7]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='new-account-form']/div[2]/div/div/div/label/input").click()
time.sleep(2)
driver.find_element(By.ID, "submit").click()
time.sleep(2)
success = driver.find_element(By.XPATH, "//*[@id='alerts-container']/div[1]")
if success is None:
    print("Не удалось открыть счет")
else:
    print("Счет открыт успешно")