from bestconfig import Config
from fastapi import FastAPI


conf = Config('.env')

app = FastAPI()
