from time import sleep
from pytest_bdd import given,parsers,when,then,parser,scenario,feature
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(60)


@given(parsers.parse("我有一个开发方账号 用户名:{username} 密码:{password}"))
def user(username,password):
    return dict(username=username,password=password)


@when(parsers.parse("打开登录页面 {url}"))
def gotourl(url):
    driver.get("http://10.10.12.154:9901")
    sleep(10)


@when(parsers.parse("输入用户名"))
def input_username():
    driver.find_element(By.ID, "username").send_keys('huoyan')


@when(parsers.parse("输入密码234234"))
def input_password():
    driver.find_element(By.ID, "password").send_keys('P@ssw0rd')


@when(parsers.parse("点击登录按钮"))
def click_login():
    driver.find_element(By.ID, "kc-login").click()


@then("判断页面中是否有登出按钮")
def try_login():
    elements = driver.find_elements(By.CSS_SELECTOR, "#app > div.menu-wrapper > div > div.icon-wrapper > span")
    assert len(elements) > 0  # 判断是否登录成功



@scenario("login.feature","正常登录")
def test_login():
    pass