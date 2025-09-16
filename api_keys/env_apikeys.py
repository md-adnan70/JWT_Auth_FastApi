from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic_settings import BaseSettings #BaseSettings is a great utility that reads environment variables and casts them to the correct type

class Settings(BaseSettings):
    api_key: str


    class Config:  #The Config class tells pydantic to read from a .env file
        env_file = '.env'

settings = Settings()

app = FastAPI()

def get_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key

@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {'output':'Access Granted'} 