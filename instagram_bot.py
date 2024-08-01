from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def drive_init():
    try:
        driver = webdriver.Firefox()  # ou webdriver.Chrome()
        return driver
    except Exception as e:
        print(f"Erro ao iniciar o driver: {e}")
        return None

def login_instagram(driver, username, password):
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao fazer login: {e}")

def navigate_to_profile(driver, profile_url):
    try:
        driver.get(profile_url)
        time.sleep(2)
    except Exception as e:
        print(f"Erro ao navegar para o perfil: {e}")

def comment_on_last_post(driver, comment_text):
    try:
        last_post = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "x1lliihq.x1n2onr6.xh8yej3.x4gyw5p.xfllauq.xo2y696.x11i5rnm.x2pgyrj"))
        )
        last_post.click()
        time.sleep(1)

        comment_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Adicione um comentário...']"))
        )

        actions = ActionChains(driver)
        actions.move_to_element(comment_area)
        actions.click()
        actions.send_keys(comment_text)
        actions.send_keys(Keys.RETURN)
        actions.perform()

        time.sleep(1)
        driver.back()
        time.sleep(2)
    except Exception as e:
        print(f"Erro ao comentar na última postagem: {e}")

def check_new_post(driver, last_posted_img_src, comment_text):
    try:
        driver.refresh()
        time.sleep(3)
        new_last_post_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_aagv"))
        )

        new_last_post_img = new_last_post_container.find_element(By.TAG_NAME, "img")
        new_last_post_img_src = new_last_post_img.get_attribute("src")
        print(f"Último src da imagem na memória: {new_last_post_img_src}")

        if new_last_post_img_src != last_posted_img_src:
            comment_on_last_post(driver, comment_text)
            last_posted_img_src = new_last_post_img_src

        return last_posted_img_src
    except Exception as e:
        print(f"Erro ao verificar novas postagens: {e}")
        return last_posted_img_src

def main():
    username = "seuusario"
    password = "suasenha"
    profile_url = "https://www.instagram.com/breuvintage/"
    comment_text = "Eu quero"
    last_posted_img_src = "https://scontent-gru1-2.cdninstagram.com/v/t51.29350-15/450235559_464319063001736_821565827324518215_n.webp?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MCJ9&_nc_ht=scontent-gru1-2.cdninstagram.com&_nc_cat=108&_nc_ohc=2n6yJWLs3ZoQ7kNvgHBtN0G&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzQxMDIwOTQ3MTI5NTAwMDMyMw%3D%3D.2-ccb7-5&oh=00_AYDY26FBVCNkTPuNcWF4UsK3wK6545iUngyocnY0VMHyQQ&oe=6696B381&_nc_sid=8f154"

    driver = drive_init()
    if driver:
        login_instagram(driver, username, password)
        navigate_to_profile(driver, profile_url)

        while True:
            last_posted_img_src = check_new_post(driver, last_posted_img_src, comment_text)
            time.sleep(5)

        driver.quit()

if __name__ == "__main__":
    main()
