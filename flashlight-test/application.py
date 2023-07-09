import json
import uvicorn
from fastapi import (FastAPI,
                     Request,
                     WebSocketDisconnect)
from fastapi.templating import Jinja2Templates

from utils import CommandChoice
from conn_manage import (manager,
                         WebSocket)
from models import Form


app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get("/")
async def get_page(request: Request):
    return templates.TemplateResponse('main.html',
                                      {'request': request})


@app.post("/", response_model=Form)
async def send_command(form: Form):
    return form


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    circle_color = 'white'
    try:
        while True:
            data = await websocket.receive_json()
            if data['command'] == CommandChoice.ON:
                circle_color = "yellow"
            elif data['command'] == CommandChoice.OFF:
                circle_color = "white"
            elif data['command'] == CommandChoice.COLOR:
                if data['metadata']:
                    circle_color = data['metadata']
            res = {'command': data['command'], 'metadata': circle_color}
            await websocket.send_json(res)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")

if __name__ == "__main__":
    uvicorn.run(app='application:app', host="127.0.0.1", port=9999,
                reload=True)
