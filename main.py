from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse('index_start.html', {'request': request, 'message': "Hi FastAPI !!!"})
