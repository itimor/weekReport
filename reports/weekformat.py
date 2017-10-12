# -*- coding: utf-8 -*-
# author: itimor
# desc: computer week by today

import datetime

def get_week_count(at=datetime.datetime.now()):
    return at.isocalendar()[1]

def get_this_monday():
    today = datetime.date.today()
    weekday = today.weekday()
    return today-datetime.timedelta(weekday)

def get_this_sunday():
    return get_this_monday() + datetime.timedelta(days=6)

def get_last_week():
    return datetime.datetime.now() - datetime.timedelta(days=7)

def get_last_week_monday():
    return get_this_monday() - datetime.timedelta(days=7)

def get_last_week_sunday():
    return get_this_sunday() - datetime.timedelta(days=7)