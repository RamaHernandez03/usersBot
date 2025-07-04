from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


USERNAME = 'ig_user123'
PASSWORD = 'ig_password'

# Cambiar .txt por el archivo generado anteriormente.
with open('example.txt', 'r') as file:
    followers_list = file.readlines()


followers_list = [follower.strip() for follower in followers_list]


driver = webdriver.Chrome()

try:

    driver.get("https://www.instagram.com/")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(10)

    # Omitir ventanas emergentes
    try:
        driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
        time.sleep(2)
    except:
        pass

    # Recorre la lista de seguidores y los sigue
    follow_count = 0  # Contador de personas seguidas
    max_follows = 60  # Máximo de personas a seguir

    for user in followers_list:
        if follow_count >= max_follows:
            print("Se alcanzó el límite de 60 personas seguidas. Finalizando el programa.")
            break

        try:
            # Navegar al perfil del usuario
            driver.get(f"https://www.instagram.com/{user}/")
            time.sleep(3)

            # Hacer clic en el botón de seguir.
            follow_button = driver.find_element(By.XPATH, "//button[normalize-space()='Seguir' or normalize-space()='Follow']")
            if follow_button:
                follow_button.click()
                follow_count += 1
                print(f"Siguiendo a {user} ({follow_count}/{max_follows})")
                time.sleep(2)  # Esperar para no hacer las peticiones demasiado rápido.
            else:
                print(f"Ya sigues a {user} o no se puede seguir.")
        except Exception as e:
            print(f"No se pudo seguir a {user}: {str(e)}")

finally:
    driver.quit()
