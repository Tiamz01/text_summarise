from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummarizer.pipeline.prediction import Predictionpipeline


text:str = "Explain Text Summariation"

app = FastAPI()
@app.get('/', tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

 
@app.get("/train")
async def training():
    try:
        os.system('python main.py')
        return Response('Training successfully completed!!')

    except Exception as e:
        return Response(f"Error Occurred! {e}")   
    


@app.post("/predict")
async def predict_route(text):
    try: 
        obj = Predictionpipeline()
        text =  obj.predict(text)
        return text
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port =8080)