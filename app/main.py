from fastapi import FastAPI
from app.database.base import Base
from app.database.database import engine
from app.models.user import User
from app.router.user_router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Python Login API is running"
    }
    
@app.get("/database-test")
def database_test():
    try:
        with engine.connect():
            return{
                "message": "Database connected successfully with pgAdmin"
            }   
    except Exception as e:
        return{
            "message": "Database connection failed",
            "error": str(e)
        }            