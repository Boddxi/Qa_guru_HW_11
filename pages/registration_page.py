from selene import browser, have
from data.users import User, Gender, Hobby
from utils.resourses import get_resource_path


class RegistrationPage:

    def __init__(self):
        self.field_first_name = browser.element('#firstName')
        self.field_last_name = browser.element('#lastName')
        self.field_user_email = browser.element('#userEmail')
        self.gender_male = browser.element('label[for="gender-radio-1"]')
        self.gender_female = browser.element('label[for="gender-radio-2"]')
        self.gender_other = browser.element('label[for="gender-radio-3"]')
        self.field_mobile_number = browser.element('#userNumber')
        self.field_subjects = browser.element('#subjectsInput')
        self.check_box_hobbies_sports = browser.element('label[for="hobbies-checkbox-1"]')
        self.check_box_hobbies_reading = browser.element('label[for="hobbies-checkbox-2"]')
        self.check_box_hobbies_music = browser.element('label[for="hobbies-checkbox-3"]')
        self.button_picture_selection = browser.element('#uploadPicture')
        self.field_current_address = browser.element('[placeholder="Current Address"]')
        self.button_submit = browser.element('#submit')
        self.value_modal_window_result = browser.all('.table-responsive tbody tr td')

    def open(self):
        browser.open(f"{browser.config.base_url}/automation-practice-form")

    def chose_date_of_birth(self,date_of_birth):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').all('option')[date_of_birth.month-1].click()
        browser.element('.react-datepicker__year-select').element(f'option[value="{date_of_birth.year}"]').click()
        browser.element(f'.react-datepicker__day--0{date_of_birth.day}').click()

    def chose_state(self,state):
        browser.element('[class=" css-1hwfws3"]').click()
        browser.element(f'//div[contains(text(), "{state}")]').hover().click()

    def choose_city(self,city):
        browser.element('[class=" css-yk16xz-control"]').click()
        browser.element(f'//div[contains(text(), "{city}")]').hover().click()

    def _select_gender(self, gender: Gender):
        gender_selectors = {
            Gender.MALE: self.gender_male,
            Gender.FEMALE: self.gender_female,
            Gender.OTHER: self.gender_other
        }
        gender_selectors[gender].click()

    def _select_hobby(self, hobby: Hobby):
        hobby_selectors = {
            Hobby.SPORTS: self.check_box_hobbies_sports,
            Hobby.READING: self.check_box_hobbies_reading,
            Hobby.MUSIC: self.check_box_hobbies_music
        }
        hobby_selectors[hobby].click()


    def register(self, user: User):
        self.field_first_name.type(user.first_name)
        self.field_last_name.type(user.last_name)
        self.field_user_email.type(user.email)
        self._select_gender(user.gender)
        self.field_mobile_number.type(user.mobile_number)
        self.chose_date_of_birth(user.date_of_birth)
        self.field_subjects.type(user.subject.value).press_enter()
        self._select_hobby(user.hobby)
        self.button_picture_selection.set_value(get_resource_path(user.picture))
        self.field_current_address.type(user.current_address)
        self.chose_state(user.state)
        self.choose_city(user.city)
        self.button_submit.click()

    def should_have_registered(self, user: User):
        formatted_date = user.date_of_birth.strftime('%d %B,%Y')
        self.value_modal_window_result.should(have.texts(
            'Student Name', f'{user.first_name} {user.last_name}',
            'Student Email', user.email,
            'Gender', user.gender.value,
            'Mobile', user.mobile_number,
            'Date of Birth', formatted_date,
            'Subjects', user.subject.value,
            'Hobbies', user.hobby.value,
            'Picture', 'file_1.txt',
            'Address', user.current_address,
            'State and City', f"{user.state} {user.city}"
        ))