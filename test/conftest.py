import pytest
from Library.config import Config
from selenium import webdriver

@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):
    if request.param == "Chrome":
        d_obj = webdriver.Chrome(executable_path = Config.Chrome_path)

    elif request.param == "Edge":
        d_obj = webdriver.Edge(executable_path = Config.Edge_path)

    d_obj.get(Config.Url)
    d_obj.maximize_window()
    yield d_obj
    d_obj.implicitly_wait(30)
    d_obj.save_screenshot("test_Ajioscreenshot.png")
    print(d_obj.title)
    d_obj.close()