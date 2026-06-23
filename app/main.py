from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text:str

@app.post("/detect")
def detect_language(data: TextRequest):
    text_lower = data.text.lower()

    if "hola" in text_lower:
        return{"language":"Spanish"}
    elif "bonjour" in text_lower:
        return{"language":"French"}
    else:
        return {"language":"Unknown"}
