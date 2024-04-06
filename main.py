from fastapi import FastAPI
from routes.students_routes import router



app = FastAPI()


app.include_router(router)

@app.get("/")
def home():
    return {
        'msg': "welcome"
    }