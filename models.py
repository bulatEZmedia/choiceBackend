from peewee import *

db = SqliteDatabase('db/database.db')



class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    gender = CharField()
    birthday = DateField()
    class Meta:
        db_table = 'users'

class AdditionalInformation(BaseModel):
    email = CharField()

    height = CharField(verbose_name="Рост")
    currentWeight = CharField(verbose_name="Масса сейчас")
    desiredWeight = CharField(verbose_name="Желаемая масса")
    physicalLimitations = CharField(verbose_name="Физические ограничения")
    body = CharField(verbose_name="Телосложение")
    bodyPart = CharField(verbose_name="Активность в течение дня")
    mostOfTheDay = CharField(verbose_name="Уровень энергии")
    foodOfTheDay = CharField(verbose_name="Физическая активность по дням")
    badHabits = CharField(verbose_name="Идеальный вес(год)")
    physActivity = CharField(verbose_name="Области тела")
    mainEvent= CharField(verbose_name="Сон")
    dateEvent = CharField(verbose_name="Тип диеты")
    yourGoal = CharField(verbose_name="Вредные привычки")
