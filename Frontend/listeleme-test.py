#Gerekli kütüphaneler import ediliyor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

# Web sürücüsünü başlatma
driver = webdriver.Chrome()

# Flight App sayfası açılıyor
driver.get("https://flights-app.pages.dev/")

# "From" ve "To" alanları için seçenekler
from_options = ["Istanbul", "New York", "London", "Paris", "Tokyo", "Sydney", "Los Angeles", "Chicago", "Beijing", "Dubai", "Singapore", "Hong Kong", "Frankfurt", "Madrid", "Rome"]
to_options = ["Istanbul", "New York", "London", "Paris", "Tokyo", "Sydney","Los Angeles", "Chicago", "Beijing", "Dubai", "Singapore", "Hong Kong", "Frankfurt", "Madrid", "Rome"]

test_successful = True  # Başlangıçta test başarılı kabul ediliyor

try:
    for from_option in from_options:
        for to_option in to_options:
            if from_option != to_option:  # Aynı şehirler seçilmesini önleniyor
                # "From" alanına şehir seçiliyor
                from_input = driver.find_element("id", "headlessui-combobox-input-:Rq9lla:")
                from_input.clear()
                from_input.send_keys(from_option)
                from_input.send_keys(Keys.RETURN)

                time.sleep(0.001)  # Seçimleri görmek için bekelme süresi ekleniyor

                # "To" alanına şehir seçiliyor
                to_input = driver.find_element("id", "headlessui-combobox-input-:Rqhlla:")
                to_input.clear()
                to_input.send_keys(to_option)
                to_input.send_keys(Keys.RETURN)

                time.sleep(0.001)  # Seçimleri görmek için bekeleme süresi ekleniyor

                try:
                    # "Found X items" yazısı alınıyor
                    found_items = driver.find_element("xpath", "//p[contains(text(), 'Found ')]").text

                    # X değeri alınıyor
                    found_items_count = int(found_items.split(" ")[1])

                    # Uçuş bulunup bulunmadığı kontrol ediliyor
                    if found_items_count > 0:
                        # BeautifulSoup ile sayfadaki HTML'i alınıyor
                        page_html = driver.page_source

                        # BeautifulSoup ile HTML işleniyor
                        soup = BeautifulSoup(page_html, 'html.parser')

                        # <li> elementlerini buluyoruz
                        li_elements = soup.find_all('li')

                        # Sayfada bulunan <li> elementlerinin sayısını belirliyoruz
                        li_count = len(li_elements)

                        # Bulunan "X" değeri ve uçuş listesi sayısı karşılaştırılıyor
                        if li_count != found_items_count:
                            test_successful = False
                            print(f"Test Başarısız: {from_option} - {to_option} için toplam {li_count} adet uçuş bulundu, ancak {found_items_count} adet bekleniyordu")
                
                except NoSuchElementException:
                    pass  # Bazı şehirler için uçuş bulunmadığı için bu durum göz ardı ediliyor

finally:
    # Tarayıcı kapatılıyor
    driver.quit()

# Tüm şehir seçenekleri için testler tamamlandıktan sonra test sonucu bastırılıyor
if test_successful:
    print("Tüm testler başarılı!")
else:
    print("Bir veya daha fazla test başarısız.")
