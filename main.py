from urllib.parse import unquote
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from peewee import *
import pydantic
from playhouse.shortcuts import model_to_dict
from models import *

import re

db = SqliteDatabase("db/database.db")

app = FastAPI()

with db:
    db.create_tables([User, AdditionalInformation])


    @app.post("/register")
    def register(email: str, password: str, name: str, gender: str, birthday: str):
        pattern = "^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$"
        match = re.fullmatch(pattern, email)
        if match:
            register = [
                {"name": name, "gender": gender, "email": email, "password": password,
                 "birthday": birthday}
            ]
            return model_to_dict(User.insert_many(register).returning(User.id).execute()[0])['id']
        else:
            return 0

    @app.post("/email_checking")
    def email_checking(email: str):
        if User.select().where(User.email == email):
            for user in User.select().where(User.email == email):
                return user.id
        else:
            pattern = "^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$"
            match = re.fullmatch(pattern, email)
            if match:
                return 0
            else:
                return -1

    @app.post("/password_checking")
    def password_checking(password: str, user_id: int):
        if User.select().where(User.id == user_id):
            if User.select().where(User.password == password):
                for user in User.select().where(User.password == password):
                    return user.id
        else:
            return 0

    @app.post("/additional_information")
    def additional_information(email:str, height: str, currentWeight: str, desiredWeight: str, physicalLimitations: str, body: str, bodyPart: str, mostOfTheDay: str, foodOfTheDay: str, badHabits: str, physActivity: str, mainEvent: str, dateEvent: str, yourGoal: str):
        add_information = [
            {"email": email, "height": height, "currentWeight": currentWeight, "desiredWeight": desiredWeight, "physicalLimitations": physicalLimitations, "body": body, "bodyPart": bodyPart, "mostOfTheDay": mostOfTheDay, "foodOfTheDay": foodOfTheDay, "badHabits": badHabits, "physActivity": physActivity, "mainEvent": mainEvent, "dateEvent": dateEvent, "yourGoal": yourGoal}
        ]

        AdditionalInformation.insert_many(add_information).execute()




''' type_of_activity: str, height: int, weight_now: int, weight_want: int, physical_limit: str, body: str,
                               activity_during_the_day: str, energy_level: str, physical_activity_by_day: str, perfect_weight_year: str, body_area: str,
                               sleep_hour: str, type_of_diet: str, bad_habits: str, water: str, answer1: str, answer2: str, level_activity: int,
                               event_name: str, event_date: str'''

''' "type_of_activity": type_of_activity, "height": height, "weight_now": weight_now, "weight_want": weight_want,
             "physical_limit": physical_limit, "body": body, "activity_during_the_day": activity_during_the_day, "energy_level": energy_level,
             "physical_activity_by_day": physical_activity_by_day, "perfect_weight_year": perfect_weight_year, "boddy_area": body_area, "sleep_hour": sleep_hour,
             "type_of_diet": type_of_diet, "bad_habits": bad_habits, "water": water, "answer1": answer1, "answer2": answer2, "level_activity": level_activity,
             "event_name": event_name, "event_date": event_date '''