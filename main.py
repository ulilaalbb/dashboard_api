import uvicorn
from app import prediction_data
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Form
from pydantic import BaseModel


app = FastAPI()

class TestCase(BaseModel):
    test_data : str


@app.post("/prediction")
async def post_prediction(testcase : TestCase):
    return {prediction_data(testcase.test_data)}


if __name__ == "__main__":  

    uvicorn.run(app, host="127.0.0.1", port=8001)


# @app.get("/prediction")
# async def post_prediction():
#     return {prediction_data("Manual Unit Testing")}
