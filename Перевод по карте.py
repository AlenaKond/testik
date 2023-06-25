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
time.sleep(1)
driver.find_element(By.ID, "cards-overview-index").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10068']/div[2]/div[2]/div/div/div[1]/a/span").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='cards-list-destination-container']/div/select").click()
driver.find_element(By.XPATH, "//*[@id='cards-list-destination-container']/div/select/option[3]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='amount-form-item']/div/div/input").send_keys(100)
time.sleep(1)
driver.find_element(By.ID, "forward").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='card-to-card-payment-form']/div[3]/div/div/div/label/input").click()
time.sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='confirmation-frame']"))
driver.find_element(By.XPATH, "//*[@id='confirm']").click()
time.sleep(3)
success = driver.find_element(By.XPATH, "//*[@id='alerts-container']/div[1]")
if success is None:
    print("Перевод отклонен")
else:
    print("Успешный перевод")

