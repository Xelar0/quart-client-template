import asyncio
import logging

from quart import Quart
from common.auth.auth import authenticate
from common.grpc_client.grpc_client import grpc_stream

app = Quart(__name__)
token = authenticate()

logging.basicConfig(level=logging.INFO)

@app.before_serving
async def startup():
    app.background_task = asyncio.create_task(grpc_stream(token))
    #init_cyoda(token)

@app.after_serving
async def shutdown():
    app.background_task.cancel()
    await app.background_task

#put_application_code_here

if __name__ == '__main__':
    app.run()
