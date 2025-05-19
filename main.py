from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse  # optional but good practice

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # No leading slash

@app.get("/", response_class=HTMLResponse)
async def form_post(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

