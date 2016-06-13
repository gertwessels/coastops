# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:19:00 2016

@author: gwessels
"""

from os.path import expanduser
from os.path import exists
from os.path import isfile
from os import makedirs
from datetime import datetime


def log(location, msg):
    """ Add msg to a log file
        Takes 2 arguments:  location = function/class from where message is logged
                            msg = Message to be logged
    """
    message  = ">> " + location + "::  "+datetime.now().strftime("%H:%M:%S, %d %B %Y")
    message += ".\n\t" + msg + "\n ==================================== \n\n"
    write_to_log(message)
    
def exception(location, exception):
    """ Add an exception to a log file
        Takes 2 arguments:  location = function/class from where message is logged
                            exception = exception object
    """
    message  = "EXCEPTION >> " + location + "::  "+datetime.now().strftime("%H:%M:%S, %d %B %Y")
    message += ".\n\t" + str(type(exception)) + "\n\t" + str(exception) + "\n ==================================== \n\n"
    write_to_log(message)

def debug(location, msg):
    """ Add msg to a log file
        Takes 2 arguments:  location = function/class from where message is logged
                            msg = Message to be logged
    """
    message  = "DEBUG >> " + location + "::  "+datetime.now().strftime("%H:%M:%S, %d %B %Y") 
    message += ".\n\t" + msg + "\n ==================================== \n\n"
    write_to_log(message)


def write_to_log(text):
    """ Writes 'text' to the beginning of the current log file"""
       
#    Define filename ( Month.year)
    filename = datetime.now().strftime("%B.%Y")
    
#    Find user's home directory    
    home = expanduser("~")
    
#    Directory
    directory = home+"/.coastops_log/"
    
#    Create .log directory if it does not exist.
    if not exists(directory):
        makedirs(directory)

#    Check if file exist before trying to read it
    if isfile(directory+filename):
        with open(directory+filename,'r') as r:
            log = r.read()
    else:
        log = ""
        
#   Write everything back to the file with the latest entry at the beginning of the file
    with open(directory+filename,'w') as w:
        w.write(text+log)
        
   