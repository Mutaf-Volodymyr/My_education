from datetime import date

from pydantic import BaseModel, EmailStr, Field, field_validator
from re import search


class AddressModel(BaseModel):
    city: str = Field(..., max_length=50)
    street: str = Field(None, min_length=6, max_length=50)
    house_number: int = Field(None, ge=1)

    class Config:
        str_min_length = 3



class UserModel(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=0, le=100)
    email: EmailStr
    password: str =  Field(..., min_length=20, max_length=50)
    address: AddressModel
    # birth_date: date

    @field_validator('email')
    def validate_email(cls, value: str):
        if value.endswith('.com'):
            return value
        # valid_emails = ['gmail', 'example']
        # if any(search(fr'@{el}\.', value) for el in valid_emails):
        #     return value
        raise ValueError('Email address is not valid')

    @field_validator('name')
    def validate_name(cls, value, values):
        if value.isalpha():
            return value
        raise ValueError('Name  is not valid')



class AdministratorModel(UserModel):
    is_admin: bool = Field(False)
    level: int = Field(1, ge=1, le=10)


if __name__ == '__main__':
    admin = UserModel(
        name="John",
        age=22,
        email="john.doe@example.com",
        password="df8h6af8fh54h7s6h7a4ha56h4sh65ad4hwdy",
        address=AddressModel(
            city="New York",
            street="5th Avenue",
            house_number=123
        ),
        is_admin=True,
        level=3
    )

    # print(admin)
    json_string = """{
        "name": "Li",
        "age": 55,
        "email": "lihong@example.com",
        "password": "df8h6af8fh54h7s6t436t326ad4",
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 146
        },
        "is_admin": true,
        "level": 10
    }"""

    admin2 = UserModel.model_validate_json(json_string, strict=True)
    # print(admin2)
