import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from pages.homePage import homePage
from config.config import Env_Variables


def test_openHome():
    random = homePage()
    random.load()
    random.click_repositories()
    last_dict = random.find_repository_records()
    print("="*20)
    print("Elements collection length: ",last_dict)
    print("="*20)
    random.closeDriver()
    