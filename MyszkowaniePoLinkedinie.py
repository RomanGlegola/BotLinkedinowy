import time
from random import randint, random

from bs4 import BeautifulSoup
from marshmallow.compat import urlparse
from selenium import webdriver
from Logowanie import wlacz_przegladarke


def myszkujemy(driver):
    wejdz_na_konto(driver)


def wejdz_na_konto(driver):
    try:
        return driver.find_element_by_xpath("/html/body/div[6]/div[6]/div[3]/div/div/div/aside[1]/div[1]/div/div[1]").click()
    except:
        print("Nie udało się wejść na konto profilowe")


def wejdz_na_profil_odwiedzajacego():
    while True:
        pass
