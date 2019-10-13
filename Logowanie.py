from selenium import webdriver


def wlacz_przegladarke():
    try:  # włącz przeglądarkę i wejdź na stronę
        driver = webdriver.Chrome(
            "Przegladarka/chromedriver.exe")
        driver.get(
            "https://www.linkedin.com")
        from Przegladarka.Opcje import opcje
        opcje(driver)
        return driver
    except:
        print("Błąd przy włączaniu przeglądarki lub strony")


def zaloguj_sie(login, haslo, driver):
    try:  # kliknij przycisk do panelu logowania
        driver.find_element_by_css_selector(
            "body > nav > a.nav__button-secondary") \
            .click()
    except:
        print("Nie znaleziono przycisku do panelu logowania")

    try:  # wpisz login
        driver.find_element_by_css_selector(
            "#username") \
            .send_keys(login)
    except:
        print("Nie znaleziono pola do wpisania loginu")

    try:  # wpisz hasło
        driver.find_element_by_css_selector(
            "#password") \
            .send_keys(haslo)
    except:
        print("Nie znaleziono pola do wpisania hasła")

    try:  # kliknij przycisk "zaloguj"
        driver.find_element_by_css_selector(
            "div.login__form_action_container > button") \
            .click()
    except:
        print("Nie znaleziono przycisku do zalogowania")


def wyloguj_sie(driver):
    try:  # wyloguj się z portalu
        driver.get("https://www.linkedin.com/m/logout/")
    except:
        print("Nie udało się wylogować z portalu")
    finally:
        driver.close()
