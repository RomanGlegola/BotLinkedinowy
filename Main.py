from Logowanie import wlacz_przegladarke, \
    zaloguj_sie, \
    wyloguj_sie
from MyszkowaniePoLinkedinie import myszkujemy

driver = wlacz_przegladarke()
zaloguj_sie("adres_email_linkedin", "hasło_linkedin", driver)

myszkujemy(driver)

wyloguj_sie(driver)
