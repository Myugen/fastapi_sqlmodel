from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
async def hello():
    return {'message': 'Hello World'}


@app.get('/hello/{specific_message}')
async def hello_with_specific_message(specific_message):
    return {'message': f'Hello, {specific_message}'}
