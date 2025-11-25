import allure
from pages.registration_page import RegistrationPage
from data.users import student

@allure.feature("Регистрация пользователя")
def test_student_registration_form(browser_management):
    registration_page = RegistrationPage()

    with allure.step('Открыть страницу регистрации'):
        registration_page.open()

    with allure.step('Зарегистрировать пользователя'):
        registration_page.register(student)

    with allure.step('Проверить зарегистрирован ли пользователь'):
        registration_page.should_have_registered(student)






