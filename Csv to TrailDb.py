
# Make sure that the python file and the csv are in same folder.

from traildb import TrailDBConstructor, TrailDB
from uuid import uuid4
from datetime import datetime
import csv

COLUMNS = ["ip","date","time","zone","cik","accession","extention","code","size","idx","norefer","noagent","find"]
cons = TrailDBConstructor('outputfile.tdb', COLUMNS) 
input_path='sample.csv'

with open(input_path) as input_file:
    reader = csv.reader(input_file)
    next(reader)
    for line in reader:
        ts = line[date]+’ ‘+line[time] 
        uuid = uuid4().hex
        ip = line[0]
        date = line[1]
        time=line[2]
        zone = line[3]
        cik= line[4]
        accession =line[5]
        extension =line[6]
        code =line[7]
        size =line[8]
        idx =line[9]
        norefer =line[10]
        noagent =line[11]
        find =line[12]
        
        cons.add(uuid, datetime.strptime(ts,'%Y-%m-%d %H:%M:%S') (ip,date,time,zone,cik,accession,extension,code,size,idx,norefer,noagent,find))
cons.finalize()
