from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from db_manager import DBManager
from pass_data import PassData

class PassData(BaseModel):
    name: str
    description: str
app = FastAPI()

db_manager = DBManager()

@app.post("/submitData")
def submit_data(pass_data: PassData):
    try:
        query = """
        INSERT INTO passes (name, location, height, status)
        VALUES (%s, %s, %s, 'new') RETURNING id;
        """
        params = (pass_data.name, pass_data.location, pass_data.height)
        db_manager.execute_query(query, params)
        return {"message": "Pass added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))