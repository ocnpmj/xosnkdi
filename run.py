
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import csv
import string
import random
import sys
import os
import names

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "sk1"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


# Fungsi membaca CSV dengan rentang baris tertentu
def read_csv_range(filename, start, end):
    with open(filename, newline='', encoding='utf-8') as f:
        rows = [row[0] for i, row in enumerate(csv.reader(f)) if start <= i < end]
    return rows

start_row = 1550
end_row = 1600

email = "jean_sturm@yahoo.com"



# Baca judul video sesuai rentang yang diinginkan
titles = read_csv_range("x.csv", start_row, end_row)

# Inisialisasi WebDriver

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)




namadepan = names.get_first_name()
namabelakang = names.get_last_name()
gmailnya = f'{namadepan}{random_string(5)}@gmail.com'

driver.get(f"https://kdi.umn.edu/register")
       
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']").send_keys(namadepan)
time.sleep(1)


driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(namabelakang)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(namadepan+random_string(5))
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Pronouns']").send_keys('Mr')
time.sleep(1)


driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email Address']").send_keys(gmailnya)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys('CobaGas123OKx')
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys('CobaGas123OKx')
time.sleep(1)


#angre

driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/form/button').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/form/div[1]/div/div/div[6]/div').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/form/div[2]/button').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="radix-:rg:"]/form/div/div/div[3]/div[1]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="radix-:rg:"]/form/button').click()
time.sleep(2)


driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/form/button').click()
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/div[2]/button[2]').click()
time.sleep(7)


# Proses upload
for title in titles:


    try:
        kw = title

        username =  kw.replace(" ", "_")

        fix_username = username+'-'+random_string(5)

        judul =f'{kw} Leaked Onlyfans New Files Update {random_string(5)}' 

        slug = judul.replace(' ','-')
        slug2 = slug.replace(".","")
        hasil_url = slug2.lower()
        

        


        driver.get("https://kdi.umn.edu/project-builder")
        time.sleep(5)
        

        driver.find_element(By.CSS_SELECTOR, "input[name='projectTitle']").send_keys(judul)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "input[name='projectTitle']").send_keys(Keys.ENTER)
        time.sleep(4)


        
        

        konten = f'''
        {judul} 
        LINK ⏩⏩ https://clipsfans.com/{username}

    '''


        

        driver.find_element(By.CSS_SELECTOR, 'div.ck-editor__editable[contenteditable="true"]').send_keys(konten)
        time.sleep(5)

        for _ in range(4):
            try:
                driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div[2]/div[2]/div/button[2]').click()
                time.sleep(3)
            except:
                pass

        driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/div[3]/div[2]/div/button[2]').click()
        time.sleep(3)

        driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[3]/a[2]').click()
        time.sleep(2)


        
    

        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": 'https://kdi.umn.edu/projects/'+hasil_url})
            .execute()
        )

     
        time.sleep(5)
    except:
        print("Terjadi error")
        

        
