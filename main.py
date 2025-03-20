from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {'message': 'Welcome !'}

@app.get('/greet/{name}')
async def greet_name(name):
    return {'message': f'Hello {name}'}