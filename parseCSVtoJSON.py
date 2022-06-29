import pandas as pd
import json

def convertBytesToString(bytes):
    df = pd.read_excel(bytes, engine="odf")
    return parse_csv(df)

def parse_csv(df):
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    return parsed