#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os
import psutil

from settings import KEYBORD, MOUSE


def is_open(path):
    """This function iter through processes and check whether there is connection with db"""
    for proc in psutil.process_iter():
        try:
            files = proc.get_open_files()
            if files:
                for _file in files:
                    if _file.path == path:
                        return True
        except psutil.NoSuchProcess as err:
            print(err)
    return False


def create_database(path: str='database', name: str="data_logs.db"):
    if not os.path.exists(os.path.join(path, name)):
        conn = sqlite3.connect('database/data_logs.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE mouse (
                time_of_event: text,
                key_data: text
            )""")

        """
        time_span: value in ms (think about making it integer)
        side: 0 -> right      1 -> left
        """
        cursor.execute("""
            CREATE TABLE keyboard (
                time_of_event: text,
                time_span: real,
                side: integer, 
                position_x: integer,
                position_y: integer
            )
        """)


def add_to_database(path: str, data, event_type, cursor=None):
    """
    This function add event to database.
    Variable event_type describe whether data should be stored in mouse or keyboard database
    """

    if not is_open(path):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
    cursor.execute("""INSERT INTO """)

    if event_type == KEYBORD:
        #TODO

        pass
    elif event_type == MOUSE:
        #TODO
        pass
    else:
        """Error Handling or other specification"""
        return False

    return True


create_database()
# con = sqlite3.connect('temp.db')
#
#
#
# con = sqlite3.connect('temp.db')
#
# path = os.path.abspath('temp.db')
#
# print(is_open(path))
# con.close()
# print(is_open(path))

# def create_database():
#     """"""
#
# def add_to_database(path: str):
#     if sqlite3.connect()
