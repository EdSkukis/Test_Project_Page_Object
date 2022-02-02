from .pages.main_page import MainPage
from .pages.product_page import AddProduct


def test_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page = AddProduct(browser, link)
    page.add_product_to_basket()

