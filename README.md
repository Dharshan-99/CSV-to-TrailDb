# CSV-to-TrailDb
### Traildb [linux]	     
### Install Python bindings		  
The following  examples is in  Python. you need to install the Python binding:
Initial setup:
```
	git clone https://github.com/traildb/traildb-python
  ```
Install the Python package with
```
	python setup.py install
  ```
### How does TrailDB work
TrailDB has two main modes: construction and querying.
In the construction phase all the event data to be ingested is passed to the library which divides the data internally in a set of trails. Each trail is a     indexed by a unique identifier of your choice.
All this ingested data is processed, ordered and compressed to minimize the occupied space. The result is a read only file ready to be queried.

### TrailDB

1.	While creating new TrailDB, every time we have to add two new additional columns uuid and timestamp then only it allows to store the data. The column uuid must have unique hexadecimal value for each row and the column timestamp must have timestamp value. These two columns are madatory in TrailDB, so we cant able to skip or modify these columns.

2.	The function UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware. The UUID4 function generates the random number and and hence can compromise the privacy, even though it provides uniqueness.


BENEFITS :
*	Maximize Speed 
  		TrailDB is a library, implemented in C, which allows you to query series of events at blazing speed. TrailDB is also optimized for speed of development: Use its simple API with your favorite language, in your favorite environment.

*	Minimize Space 
		TrailDB's secret sauce is data compression. It leverages predictability of time-based data to compress your data to a fraction of its original size. In contrast to traditional compression, you can query the encoded data directly, decompressing only the parts you need.
## Creating simple TrailDB
Inside the TrailDBConstructor we declare _'tiny'_ as the output TrailDb file and _'username' 'action'_ as columns._uuid_ as hexadecimal number and username(i=3 so only three users). 
```
cons = TrailDBConstructor('tiny',['username', 'action'])
	for i in range(3):
    uuid = uuid4().hex
    username = 'user%d' % i
    for day,action in enumerate(['open','save','close']):
        cons.add(uuid, datetime(2016, i + 1, day + 1),(username, action))
    cons.finalize()

```
Finally the tdb file columns are uuid,datetime,username and action.
		
		
## CSV to TrailDb	
The following packages are need to be installed for TrailDB creation.
```
	From traildb import traildbconstructor.
	From uuid import uuid4
	From datetime import datetime
```
Add all columns in the form of list
```
 columns=["ip","date","time","zone","cik","accession","extention","code","size","idx","norefer","noagent","find"]
 ```
 Declare the output file name and column list inside the TrailDBConstructor
 ```
 cons = TrailDBConstructor('outputfile.tdb', COLUMNS)
 ```
 Input csv file name
 ```
 input_path='sample.csv'
 ```
 Reading the Csv File using csv reader
 ```
 with open(input_path) as input_file:
    reader = csv.reader(input_file)
    next(reader)
  ```
Access the columns in the csv file and add it to the constructor:    
    
  ```
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
```
close the constructor:
```
cons.finalize()
```
  
    
 
 
   


 




