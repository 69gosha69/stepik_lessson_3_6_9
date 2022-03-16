import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_button_add_basket(browser):
    browser.get(link)
    #time.sleep(30)
    button_add_basket = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert button_add_basket, "Button not found"
