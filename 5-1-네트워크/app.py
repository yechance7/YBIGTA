from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# 데이터 저장소 (임시 데이터베이스 역할)
data_store: Dict[str, Dict] = {}

class Data(BaseModel):
    name: str
    age: int

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# 간단한 GET 요청에 대한 응답
@app.get("/hello")
async def hello_world():
    return {"message": "Hello, World!"}

# POST 요청을 받아 JSON 응답을 반환
@app.post("/data", status_code=201)
async def receive_data(data: Data):
    if data.name in data_store:
        raise HTTPException(status_code=400, detail="Data with this name already exists")
    data_store[data.name] = data.dict()
    return {"status": "success", "name": data.name, "received_data": data}

# GET 요청으로 전체 데이터 목록 조회
@app.get("/data")
async def get_all_data():
    return {"data": data_store}

# GET 요청으로 데이터 조회
@app.get("/data/{name}")
async def get_data(name: str):
    data = data_store.get(name)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"data": data}

# PUT 요청으로 데이터 수정
@app.put("/data/{name}")
async def update_data(name: str, data: Data):
    if name not in data_store:
        raise HTTPException(status_code=404, detail="Data not found")
    data_store[name] = data.dict()
    return {"status": "success", "updated_data": data}

# DELETE 요청으로 데이터 삭제
@app.delete("/data/{name}")
async def delete_data(name: str):
    if name not in data_store:
        raise HTTPException(status_code=404, detail="Data not found")
    del data_store[name]
    return {"status": "success", "deleted_name": name}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")