from fastapi import FastAPI, File, UploadFile
from parseCSVtoJSON import convertBytesToString
from Validaciones import validacion
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()
@app.on_event("startup")
async def startup():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
@app.post("/csv/")
async def parsecsv(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = convertBytesToString(contents)
    result = []
    for json in json_string:
        data = validacion(json, json['target id'])
        result.append(data)
    return {
        "file_contents": result
    }