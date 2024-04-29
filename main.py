from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import ollama

# Create FastAPI instance
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create Jinja2Templates instance
templates = Jinja2Templates(directory="templates")

# Route for home page
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Function to get completion from Ollama chat model
def get_completion(prompt):
    messages = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    res = messages['message']['content']
    return res

# Route for getting answers
@app.post("/get_answers")
async def get_answers(file: UploadFile = File(...)):
    contents = await file.read()
    questions = contents.decode().split('\n')
    answers = []
    for question in questions:
        answer = get_completion(question)
        answers.append(answer)
    return JSONResponse(answers)
