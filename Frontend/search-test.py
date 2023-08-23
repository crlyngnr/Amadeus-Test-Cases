# Gerekli kütüphaneler import ediliyor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# WebDriver başlatılıyor
driver = webdriver.Chrome()

# Flight App sayfası açılıyor
driver.get("https://flights-app.pages.dev/")

success = True  # Başarıyı izlemek için bir bayrak

try:
    # "From" ve "To" alanları için seçenekler
    from_options = ["Istanbul", "New York", "London", "Paris", "Tokyo", "Sydney", "Los Angeles", "Chicago", "Beijing", "Dubai", "Singapore", "Hong Kong", "Frankfurt", "Madrid", "Rome"]

    for from_option in from_options:
        for to_option in from_options:
            # "From" alanında seçenek seçiliyor
            from_input = driver.find_element("id","headlessui-combobox-input-:Rq9lla:")
            from_input.clear()  # Mevcut değeri temizleniyor
            from_input.send_keys(from_option)
            from_input.send_keys(Keys.RETURN)
            time.sleep(0.2)  # Seçim işleminin gözlemlenmesi için bekleniyor

            # "To" alanında seçenek seçiliyor
            to_input = driver.find_element("id","headlessui-combobox-input-:Rqhlla:")
            to_input.clear()  # Mevcut değeri temizleniyor
            to_input.send_keys(to_option)
            to_input.send_keys(Keys.RETURN)
            time.sleep(0.2)  # Seçim işleminin gözlemlenmesi için bekleniyor

            # "To" alanının değeri "From" ile aynı mı diye kontrol ediiyor
            if from_input.get_attribute("value") == to_input.get_attribute("value"):
                print(f"Hata: Aynı şehirler seçilebiliyor - From: {from_option}, To: {to_option}")
                success = False  # Hata bulunduğunda başarıyı değiştiriyor
                break  # Hata bulunduğunda iç döngüyü kırıyor

        if not success:  # Hata bulunduysa dış döngüyü de kıryor
            break

except Exception as e:
    print(f"Hata: {str(e)}")

finally:
    # WebDriver kapatılıyor
    driver.quit()

# Testin başarı durumu kontrol ediliyor
if success:
    print("Test başarılı: Aynı şehirler seçilemiyor.")
else:
    print("Test başarısız: Aynı şehirler seçilebiliyor.")
