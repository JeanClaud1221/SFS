import os
import shutil
import time
dur=120
while True:
    time.sleep(dur)
    ext=['TXT','JPG','ZIP','JPEG']
    source='C:/Users/jean-claud/Desktop/temp1'
    destination='C:/Users/jean-claud/Desktop/temp2'
    allfiles=os.listdir(source)
    for f in allfiles:
        temp=f.split('_')
        src=f'{source}/{f}'
        if temp[0] in ext:
            dest=f'{destination}/{temp[0]}/{temp[1]}'
            shutil.move(src,dest)
    


