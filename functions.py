import sqlite3
import datetime

from keys import admin_id


def create_table():  # Create Table
    """Create Applicant(abiturent) table in database.db file"""
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        create_table_query = """CREATE TABLE IF NOT EXISTS Qabul (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, name TEXT NOT NULL, phone TEXT NOT NULL);"""
        cursor.execute(create_table_query)
        connection.commit()
        print('Connected to database')


# create_table()


def insert_data(user_id, name='test', phone_number=''):
    """Insert Data Applicant(abiturent) table name and phone_number in database.db file"""
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        insert_query = """INSERT INTO Qabul (user_id, name, phone) VALUES (?, ?, ?)"""
        applicant = (str(user_id), name, phone_number)
        cursor.execute(insert_query, applicant)
        connection.commit()


# insert_data(556841744, "Ergashev Shaxzod", "+998994002599")


def read_applicant():
    """"Read Applicant(abiturent) table id, name, phone_number in database.db file"""
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        select_query = """SELECT * FROM Qabul;"""
        cursor.execute(select_query)
        applicants = cursor.fetchall()
        data = []
        for applicant in applicants:
            dat = [applicant[0], applicant[1], applicant[2], applicant[3]]
            data.append(dat)
        return data


# print(read_applicant())


def delete_applicant():
    applicants = read_applicant()
    for applicant in applicants:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            delete_query = f"""DELETE FROM Qabul WHERE id = {applicant[0]}"""
            cursor.execute(delete_query)
            connection.commit()


# delete_applicant()


def update_applicant(user_id, phone_number):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        voter_query = """UPDATE Qabul SET phone = ? WHERE user_id = ?;"""
        cursor.execute(voter_query, (phone_number, user_id))
        connection.commit()


def new_table_renessans():  # Create Table
    """Create Student(abiturent) table in database.db file"""
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        create_table_query = """CREATE TABLE IF NOT EXISTS Renessans (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, name TEXT, ages TEXT, phone TEXT, create_at DATETIME NOT NULL);"""
        cursor.execute(create_table_query)
        connection.commit()
        # print('Connected to database')


# new_table_renessans()


def insert_renessans_data(user_id, name, ages, phone, create_at):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        insert_query = """INSERT INTO Renessans (user_id, name, ages, phone, create_at) VALUES (?, ?, ?, ?, ?)"""
        applicant = (str(user_id), name, ages, phone, create_at)
        cursor.execute(insert_query, applicant)
        connection.commit()


# insert_renessans_data(admin_id, "Ergashov Botirjon", '25 da', '+998995907850', datetime.date.today())


def read_renessans_data():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        select_query = """SELECT * FROM Renessans;"""
        cursor.execute(select_query)
        students = cursor.fetchall()
        data = []
        for student in students:
            dat = [student[0], student[1], student[2], student[3], student[4], student[5]]
            data.append(dat)
        return data


# print(read_renessans_data())


def update_renessans_ages(user_id, ages):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        renessans = """UPDATE Renessans SET ages = ? WHERE user_id = ?;"""
        cursor.execute(renessans, (ages, user_id))
        connection.commit()
        # print('Connected to database')


def update_renessans_phone(user_id, phone):
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        renessans = """UPDATE Renessans SET phone = ? WHERE user_id = ?;"""
        cursor.execute(renessans, (phone, user_id))
        connection.commit()
        # print('Connected to database')


def delete_renessans():
    applicants = read_renessans_data()
    for applicant in applicants:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            delete_query = f"""DELETE FROM Renessans WHERE id = {applicant[0]}"""
            cursor.execute(delete_query)
            connection.commit()


def check_user_id(user_id):
    renessans = read_renessans_data()
    for renessan in renessans:
        if user_id == renessan[1]:
            return False
    return True
