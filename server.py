from quart import Quart, websocket
app = Quart(__name__)
@app.websocket('/')
async def ws():
    while True:
        msg = await websocket.receive()
        print(msg.strip())
