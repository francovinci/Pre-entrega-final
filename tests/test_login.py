import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize("usuario, contra, exitoso", [
    ("problem_user", "francovinci", False),
    ("standard_user", "secret_sauce", True)
])
def test_login(driver, usuario, contra, exitoso):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    ).send_keys(usuario)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "password"))
    ).send_keys(contra)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()
    
    if exitoso:
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    else:
        assert driver.current_url == "https://www.saucedemo.com/"

@pytest.mark.parametrize("usuario, contra", [
    ("standard_user", "secret_sauce")
])
def test_verificacion_titulo(usuario, contra, driver):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    ).send_keys(usuario)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "password"))
    ).send_keys(contra)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()
    try:
        aceptar_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Aceptar')]"))
    )
        aceptar_btn.click()
    except:
        pass

    time.sleep (10)
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".header .app-logo"))
    )

    # Verificación
    assert titulo.get_attribute("alt") == "Swag Labs"

