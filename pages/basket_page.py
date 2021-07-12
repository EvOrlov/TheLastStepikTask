from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_goods_in_basket(self):
        # Ищется div с товарами в корзине. Если не находится - все хорошо.
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "Have product in basket, but should not be"

    def should_be_empty_basket(self):
        # Функция работает со всеми языками. Поскольку нельзя локализовать чистый текст из тега <p> без
        # захвата довеска в теге <а>, а языком может быть иероглиф, то находятся оба текста
        # и из полного текста удаляется довесок.
        # Текущий язык берется из строки браузера, ссылка разбивается на список по "/"
        # и в ней ищется совпадение. При разности строк появляется пробел, устраняемый [:-1]
        # Для проверки работы языков, можно, к примеру в файле test_main_page.py
        # поменять ссылку на link = "http://selenium1py.pythonanywhere.com/ar/" - арабский
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "en-gb": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
            "en-US": "Your basket is empty."
        }
        local_lang = next(value for key, value in languages.items() if key in self.browser.current_url.split("/"))
        # делаем одну итерацию (next) по ключам словаря, находим совпадение с языком из строки браузера
        # возвращаем значение найденного ключа т.е.  "Your basket is empty."
        full_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        a_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_LINK_A).text
        assert local_lang == full_text.replace(a_text, "")[:-1], \
            f"'Your basket is empty' text not found, found '{full_text}' instead"
