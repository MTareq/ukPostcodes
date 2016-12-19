======Requirements=====

Python (2.7.x, 3.x), python-pip, virtualenv

======Installation=====

--Create a virtual enviroment 

$ virtualenv env 
$ source env/bin/activate

--Install the required packages as such:

$ pip install -r requirements.txt


======Third party packages used======

1- Requests (http://docs.python-requests.org/)


======postcode.py====
- function generate_from_file(file_path)==> returns a generator of PostCode objects (given a file of postcode strings per line)

- class PostCode():
	properties:
		- code
		- outcode: the outward code of the objects post code
		- info : a dictianary of information about the objects postcode
		- outward_info: a dictinary of information about the objects outward code
		- nearest_info:  an array of information dicts about the nearest post codes to the object post code
		- nearest_out_info: an array of information dicts about the nearest out codes to the objects outward code

======Usage=====
$python
>>>import postcode


>>>#single object usage
>>>mycode = postcode.PostCode("M32 0JG")
>>>mycode.info


>>>#generated from a file of codes
>>>for code in postcode.generate_from_file('./sample_codes'):
      ...:     print(code.info)
      ...:     print(code.outward_info)
      ...:     print(code.nearest_info)
      ...:     print(code.nearest_out_info)
   

======Constraint======

This library will not run offline since it depend on an external api to query post conde information

