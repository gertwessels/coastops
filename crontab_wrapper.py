# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:52:02 2016

@author: gwessels
"""

import os
import error_log as err

class CronTab:
    """ a wrapper for the crontab application"""
    
    def __init__(self, cmd, user=True, minute='5',hour='0',dayofmonth='*',month='*',dayofweek='*'):
        global MONTH = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','*']
        global DOW = ['SUN','MON','TUE','WED','THU','FRI','SAT','*']
        """ The default is a empty task, scheduled for 00:05 every day."""
        self.minute = self.__check_minute__(minute)
        self.hour = self.__check_minute__(hour)
        self.dayofmonth = self.__check_dom__(dayofmonth)
        self.month = self.__check_month__(month)
        self.dayofweek = self.__check_dow__(dayofweek)
        self.command = cmd
    
    def __check_minute__(self,minute):
        """ Check whether valid minutes value is entered """
        if not isinstance(minute,str) and not isinstance(minute,int):
            error = TypeError("minute needs to be either an int or string value, between 0-59")
            raise error
            err.exception("CronTab.__check_minute__",error)
        if isinstance(minute,int):
            if minute > 59 or minute < 0:
                error = ValueError("The minute value needs to be 0-59.")
                raise error
                err.exception("CronTab.__check_minute__",error)
        return minute
    
    def __check_hour__(self,hour):
        """ Check whether valid hour value is entered """
        if not isinstance(hour,str) and not isinstance(hour,int):
            error = TypeError("hour needs to be either an int or string value, between 0-23")
            raise error
            err.exception("CronTab.__check_hour__",error)
        if isinstance(hour,int):
            if hour > 23 or hour < 0:
                error = ValueError("The hour value needs to be 0-23.")
                raise error
                err.exception("CronTab.__check_hour__",error)
        return hour
    
    def __check_dom__(self,dom):
        """ Check whether valid day of month value is entered """
        if not isinstance(dom,str) and not isinstance(dom,int):
            error = TypeError("day of month needs to be either an int or string value, between 1-31")
            raise error
            err.exception("CronTab.__check_dom__",error)
        if isinstance(dom,int):
            if dom > 31 or dom < 1:
                error = ValueError("The day of month value needs to be 1-31.")
                raise error
                err.exception("CronTab.__check_dom__",error)
        return dom
    
    def __check_month__(self,month):
        """ Check whether valid month value is entered """
        if not isinstance(month,str) and not isinstance(month,int):
            error = TypeError("month needs to be either an int or string value, between 1-12")
            raise error
            err.exception("CronTab.__check_hour__",error)
        if isinstance(month,int):
            if month > 12 or month < 1:
                error = ValueError("The month value needs to be 1-12 or JAN-DEC or *.")
                raise error
                err.exception("CronTab.__check_month__",error)
            if isinstance(month,str):
                if month not in MONTH:
                    error = ValueError("The month value needs to be 1-12 or JAN-DEC or *.")
                    raise error
                    err.exception("CronTab.__check_month__",error)
        return dom
    
    def __check_dow__(self,dow):
        """ Check whether valid day of week value is entered """
        if not isinstance(dow,str) and not isinstance(dow,int):
            error = TypeError("day of week needs to be either an int or string value, between 0-6 where 0=Sunday")
            raise error
            err.exception("CronTab.__check_dow__",error)
        if isinstance(dow,int):
            if dow > 6 or dow < 0:
                error = ValueError("The day of week value needs to be 1-31 or SUN-SAT or *.")
                raise error
                err.exception("CronTab.__check_dow__",error)
        if isinstance(dow,str):
            if dow not in DOW:
                error = ValueError("The day of week value needs to be 1-31 or SUN-SAT or *.")
                raise error
                err.exception("CronTab.__check_dow__",error)
        return dow
    
    def commit(self):
        with open('tmp.cron','w') as f:
            task = str(self.minute)+" "+str(self.hour)+" "+str(self.dayofmonth)+" "+str(self.month)+" "+str(self.dayofweek)+" "+self.command
            f.write(task)
            
        retvalue = os.popen("crontab tmp.cron").readlines()
        
        return retvalue

