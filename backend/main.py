from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates # Esto es para crear las plantillas HTML
from fastapi.staticfiles import StaticFiles # Esto es para insertar los css y js (si los hay)

# Instancia de FastAPI
app = FastAPI(title="Hoja de Vida", version="1.0.0")

# Archivos de estilo
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Plantilla html
templates = Jinja2Templates(directory="frontend/templates")

# Ruta principal
@app.get("/")
def hojaDeVida(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})