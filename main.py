"""
This is my simple API example. 

Notes
=====
- Use endpoint to separate  concerns from resources. 

Operations 
----------
- operations are just methods of the FastAPI class
- these are http methods 

- there are 8 of them, 4 simple and 4 more complicated

-- post : create data
-- get : read data 
-- put : update data
-- delete  : delete data

-- options 
-- head 
-- patch 
-- trace

we communicate with the path (endpoint) using these methods (operations)

- path operation decorator decorates the path function with an operator method from the FastAPI class.
- path operation defines what happens at the endpoint. 
(use async if you think you might need to use await inside the function - this is a couroutine that 
tells the code thata it might need to tell the code to wait with whatever it is communicating with e.g. a database)

Running 
-------
- we run by executing uvicorn <python-module>:<api-instance> --reload e.g. main:app --reload
- reload just means everytime I save python module I recreate the api 

Using 
-----
Can then view interactive docs at http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

app = FastAPI()


# define path operation decorator - function defined below this will handle requests to <path> (which is the parameter of the decorator)
# using <operation> (which is the particular deorator used (e.g. get))
@app.get(
    "/"
)  # location of end point / path / route (i.e. everything after .com in the url)
async def root():  # define path operation function - what is executed at endpoint
    return {"message": "Hello World"}
