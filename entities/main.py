# entities/main.py

from fastapi import FastAPI
import uvicorn

# Создаем экземпляр FastAPI
app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
