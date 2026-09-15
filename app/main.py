from fastapi import FastAPI
from app.database.database import engine

app = FastAPI()

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
                "message": "Database connected successfully"
            }   
    except Exception as e:
        return{
            "message": "Database connection failed",
            "error": str(e)
        }            