import os
import pandas as pd
from datetime import datetime


location = "data"
 
ls = sorted(os.listdir("data"))

files = [item for i, item in enumerate(ls) if item.endswith('.hdf')]

tmp_wav = []
tmp_cur = []

for f in files:
    if f[13:-4] == 'currents':
        tmp_cur.append([f,datetime.strptime(f[:9],'%Y%m%d')])
    elif f[13:-4] == 'waves_wind':
        tmp_wav.append([f,datetime.strptime(f[:9],'%Y%m%d')])

file_cur = pd.Dataframe(tmp_cur,columns=["filename","date"])
file_wav = pd.Dataframe(tmp_wav,columns=["filename","date"])



#def add_record():

 

