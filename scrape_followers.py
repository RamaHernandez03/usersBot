from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura tus credenciales y la cuenta objetivo
USERNAME = 'ig_user123'
PASSWORD = 'ig_password'
TARGET_ACCOUNT = 'Im_the_target'  # La cuenta cuyos seguidores quieres obtener
FOLLOWERS_LIMIT = 3000  # Límite de seguidores a extraer, a eleccion

# Inicializa el navegador
driver = webdriver.Chrome()

try:
    # Cargar usuarios existentes desde el archivo (si existe)
    existing_followers = set()
    try:
        # Cambiar por .txt existente.
        with open("example.txt", "r") as file:
            existing_followers = set(line.strip() for line in file)
    except FileNotFoundError:
        print("No se encontró el archivo, se creará uno nuevo.")

    # Abre Instagram
    driver.get("https://www.instagram.com/")
    time.sleep(3)

    # Inicia sesión
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys('\n')
    time.sleep(5)

    # Omitir ventanas emergentes
    try:
        driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
        time.sleep(2)
    except:
        pass

    # Navega a la cuenta objetivo
    driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
    time.sleep(3)

    # Haz clic en la sección de seguidores
    followers_link = driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
    followers_link.click()
    time.sleep(3)

    # Espera hasta que el modal de seguidores sea visible
    followers_popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']"))
    )

    # Extrae los seguidores
    followers_list = []

    # Desplázate por la lista para cargar más usuarios (Importante, sino el bot no te va a detectar los users ya que ig no te los va a cargar.)
    for _ in range(int(FOLLOWERS_LIMIT / 10)):  # Ajusta el rango según el límite
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
        time.sleep(2)

    # Obtén los nombres de usuario visibles
    followers = followers_popup.find_elements(By.XPATH, "//a[contains(@href, '/')]")
    for follower in followers:
        username = follower.get_attribute("href").split("/")[-2]
        # Filtra los enlaces no relacionados con usuarios
        if username.isalnum() and len(username) > 1 and not username.startswith(('explore', 'help', 'about', 'privacy', 'terms', 'locations', 'lite', 'blog', 'inbox', 'meta', 'instagram')): 
            followers_list.append(username)
        if len(followers_list) >= FOLLOWERS_LIMIT:
            break

    # Combina las listas, eliminando duplicados
    new_followers = set(followers_list) - existing_followers

    # Guarda los nombres de usuario únicos (existentes + nuevos) en un archivo .txt // Cambiar .txt
    with open("example.txt", "a") as file:
        for user in new_followers:
            file.write(f"{user}\n")

    print(f"Nuevos usuarios agregados al archivo:")
    print(new_followers)

finally:
    driver.quit()