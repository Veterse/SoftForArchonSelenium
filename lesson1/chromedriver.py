
import random
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import os
urls = [
    "https://testnet.funkybit.fun/memejam/coins/ARCHSTROAUNT%E2%80%A2LT:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/PI%E2%80%A2NETWORK%E2%80%A2COINSSS:bitcoin",
    "https://funkybit.fun/memejam/coins/MILAAAAAAAADY:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/SPARKLE%E2%80%A2TODAY%E2%80%A2WELL:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/QUEEN%E2%80%A2BOA%E2%80%A2HANCOOK:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/TANZANIA%E2%80%A2NEW%E2%80%A2COIN%E2%80%A2SIRJADY:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/UNICORN%E2%80%A2CAT%E2%80%A2COIN:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/UNION%E2%80%A2NOSE%E2%80%A2MAN%E2%80%A2FOR%E2%80%A2U:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/REMA%E2%80%A2VS%E2%80%A2BUJU%E2%80%A2WHO%E2%80%A2IS%E2%80%A2BETTER:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/DAVECOIN%E2%80%A2G%E2%80%A2G%E2%80%A2G%E2%80%A2G%E2%80%A2G:bitcoin",
    "https://testnet.funkybit.fun/memejam/coins/ANNETA%E2%80%A2KLINGER:bitcoin",
    "https://funkybit.fun/memejam/coins/KAKARI%E2%80%A2PRIMEKKKK:bitcoin",
    "https://funkybit.fun/memejam/coins/SERGRGRBGHEGRGRE:bitcoin",
    "https://funkybit.fun/memejam/coins/BARIX%E2%80%A2BONZATIM:bitcoin",
    "https://funkybit.fun/memejam/coins/REMOVE%E2%80%A2THE%E2%80%A2TRUMP:bitcoin"



]
brave_binary = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
brave_user_data = r"C:\Users\Денис\AppData\Local\BraveSoftware\Brave-Browser\User Data"

# Функция для выполнения действий с профилем
def run_actions(driver):
   
    # Ожидание и открытие сайта
    wait = WebDriverWait(driver, 60)
    
    getter = random.choice(urls)
    print(getter)
    driver.get(getter)
    print("я открыл")
    Main = driver.current_window_handle

    # Вводим "1" в поле ввода
    wait.until(EC.visibility_of_element_located(input_for_buy)).send_keys("1")
    time.sleep(1)
    # Нажимаем кнопку "Place Trade"
    wait.until(EC.element_to_be_clickable(button_for_buy)).click()

    time.sleep(1)
    Okna = driver.window_handles

    driver.switch_to.window(Okna[2])
    print(driver.current_url)
    
    #inputpassword = driver.find_element("xpath", "//input")
    inputer = ("xpath","//input")
    print("я перешёл туда")
    time.sleep(1)
    print(Okna)
    wait.until(EC.visibility_of_element_located(inputer)).send_keys("123321qW.@##")
    time.sleep(1)
    
    


    
    print("я ввёл текст")

    wait.until(EC.element_to_be_clickable(buttonAccessPassword)).click()
    print("клик прошёл успешно")
    time.sleep(3)
    Okna = driver.window_handles
    time.sleep(1)
    driver.switch_to.window(Okna[2])
    wait.until(EC.element_to_be_clickable(ConfirmedPassword)).click()
    print("кошелёк подтверждён")
    
    

    for i in range(103):
        
        driver.switch_to.window(Main)
        print(driver.current_url)
        time.sleep(2)
        wait.until(EC.visibility_of_element_located(input_for_buy)).clear()
        time.sleep(1)
        
       
        
        wait.until(EC.visibility_of_element_located(input_for_buy)).send_keys("1")
        time.sleep(1)
        wait.until(EC.element_to_be_clickable(button_for_buy)).click()
        time.sleep(1)
        Okna = driver.window_handles
        print(i)
        
        print(Okna)
        driver.switch_to.window(Okna[2])
        wait.until(EC.element_to_be_clickable(ConfirmedPassword)).click()
    

    # Даём время на выполнение действий
    time.sleep(15)
    driver.quit()

if __name__ == "__main__":
    # Закрываем все процессы Chrome перед запуском
    os.system("taskkill /im brave.exe /f")
    time.sleep(2)
        # вот все твои текущие профили profiles = ["Default" "Profile 1","Profile 2","Profile 3","profile 4","Profile 5","Profile 6","Profile 7"]
    # Список профилей пользователей
    profiles = [ "Profile 1" ] 
    profile_path = r"C:\Users\Денис\AppData\Local\Google\Chrome\User Data"

    # Определяем элементы на странице
    input_for_buy = ("xpath", "//input[@class='w-full px-3 py-2 rounded-2xl focus:outline-none border-0 focus:ring-0 py-3 text-white [appearance:textfield] placeholder:text-mutedText [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none bg-darkBackground5 text-left text-2xl']")
    button_for_buy = ("xpath", "//button[text() = 'Place Trade']")
    inputforPassword = ("xpath", "//input")
    
    buttonAccessPassword = ("xpath", "//div[contains(@style, 'display: flex') and contains(@style, 'height: 48px') and contains(@style, 'linear-gradient(103.92deg, rgb(235, 185, 76) 0%, rgb(233, 126, 0) 100%)')]")
    ConfirmedPassword = ("xpath", "//div[contains(@style, 'display: flex') and contains(@style, 'height: 48px') and contains(@style, 'linear-gradient')]")

    # Установка ChromeDriver один раз
    service = Service(ChromeDriverManager().install())

    # Запуск для каждого профиля
    for profile in profiles:
        # Настройка опций Chrome для каждого профиля
        options = uc.ChromeOptions()
        options.binary_location = brave_binary  
        options.add_argument(f"--user-data-dir={brave_user_data}")
        options.add_argument(f"--profile-directory={profile}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

        # Запуск браузера с текущим профилем
        driver = uc.Chrome(service=service, options=options)
        run_actions(driver)
        time.sleep(2)


