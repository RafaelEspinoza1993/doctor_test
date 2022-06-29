from fastapi import FastAPI, File, UploadFile
from parseCSVtoJSON import convertBytesToString
from Validaciones import validacion

app = FastAPI()
result = []
@app.post("/csv/")
async def parsecsv(file: UploadFile = File(...)):
    contents = await file.read()
    json_string = convertBytesToString(contents)
    for json in json_string:
        data = validacion(json, json['target id'])
        result.append(data)
    return {
        "file_contents": result
    }