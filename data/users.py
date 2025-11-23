import dataclasses
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


class Subject(Enum):
    MATHS = "Maths"
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"
    ENGLISH = "English"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    date_of_birth: date
    subject: Subject
    hobby: Hobby
    picture: str
    current_address: str
    state: str
    city: str


student = User(first_name='Juliya', last_name='Smykova', email='julieta-petrova@yandex.ru',
               gender=Gender.FEMALE, mobile_number='9111177777', date_of_birth=date(1990, 2, 20),
               subject=Subject.MATHS, hobby=Hobby.SPORTS, current_address='Address', picture="file_1.txt", state='Uttar Pradesh',
               city='Merrut')
