import socket
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def phase1_login(driver, current_ip):
    """Phase 1: Fill out and submit the login form."""
    wifi_login_url = f"https://authweb.hinet.net/auth/auth_login/login1?client_ip={current_ip}"
    driver.get(wifi_login_url)

    # Wait for the page to load
    time.sleep(3)

    # Locate form fields and login button
    username_field = driver.find_element(By.NAME, "cht_user")
    password_field = driver.find_element(By.NAME, "passwd")
    login_button = driver.find_element(By.ID, "submit")

    # Fill in the username and password
    # Note: Replace with your actual username and password
    username_field.send_keys("09xxxxxxxx")
    password_field.send_keys("pwd")

    # Submit the form
    login_button.click()

    # Wait for a short time to ensure the form is submitted
    time.sleep(5)


def phase2_redirect(driver):
    """Phase 2: Handle the redirect page."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary"))
    )
    redirect_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
    redirect_button.click()


def phase3_handle_alert(driver):
    """Phase 3: Handle the alert popup."""
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Alert message: {alert_text}")

        if "您目前享有" in alert_text or "成功" in alert_text:
            print("Successfully logged in!")
        else:
            print("Login failed.")
        alert.accept()
    except Exception as e:
        print(f"An error occurred while handling the alert: {e}")
    finally:
        driver.quit()


def main():
    """Main function to execute the login process."""
    current_ip = get_ip_address()

    # Path to ChromeDriver(change to your own path)
    driver_path = (
        "C:\\Program Files\\Chrome Driver\\chromedriver-win64\\chromedriver.exe"
    )
    service = Service(driver_path)

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service)

    try:
        # Execute the three phases
        phase1_login(driver, current_ip)
        phase2_redirect(driver)
        phase3_handle_alert(driver)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        driver.quit()


if __name__ == "__main__":
    main()
