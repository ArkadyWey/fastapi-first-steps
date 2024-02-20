"""
This is my simple API example. 

Notes
-----
- Use endpoint to concerns from resources  

- operations are just methods in the FastAPI classs
-- these are http methods 
-- post : create data
-- get : read data 
-- put : update data
-- delete  : delete data

-- options 
-- head 
-- patch 
-- trace

we communicate with the path using these operations (methods)

- path operation decorator decorates the path function with a decorator from the FastAPI class.
- path operation defines what happens at the endpoint 
(use async if you think you might need to use await inside the function - this is a couroutine that 
tells the code thata it might need to tell the code to wait with whatever it is communicating with e.g. a database)
"""

from fastapi import FastAPI

app = FastAPI()


# define path operation decorator - function defined below this will handle requests to <path> using <operation>
@app.get(
    "/"
)  # location of end point / path / route (i..e everything after .com in the url)
async def root():  # path operation function - what is executed at endpoint
    return {"message": "Hello World"}
