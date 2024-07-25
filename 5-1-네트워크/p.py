https://hengyinayo.notion.site/581e31fa8fc2419fb7455805b2f02fae
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
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")      # 데이터 추가 (POST)
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 30}' http://127.0.0.1:8000/data

# 전체 데이터 조회 (GET)
curl http://127.0.0.1:8000/data

# 특정 데이터 조회 (GET)
curl http://127.0.0.1:8000/data/John%20Doe

# 데이터 수정 (PUT)
curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 35}' http://127.0.0.1:8000/data/John%20Doe

# 데이터 삭제 (DELETE)
curl -X DELETE http://127.0.0.1:8000/data/John%20Doe          **과제 1 (POST) -**

😆 오늘은 총 다섯 명의 인원이 왔네요! 😆

[23기, DE팀, 전 부대장, 이어흥]

[24기, DE팀, DE 팀장, 임채림]

[22기, DS팀, 교육부장, 김지훈]

[24기, DE팀, 부회장, 조윤영]

[24기, DS팀, 회장, 이동진]

총 5개의 항목들이 있는데요, 우리 함께 출석 체크를 해봅시다.

- gi
- team
- role
- name

url 형식:

/list

**과제 2 (GET) -**

출석부를 확인해볼까요? 🤔

url 형식:

/list

**과제 3 (PUT) -**
이어흥 → 이우흥으로 수정해보고 이우흥만 따로 확인해봅시다
url 형식:

/list/{name}

**과제 4 (DELETE) -**

이우흥을 출석부에서 지워버립시다!!! 

url 형식:

/list/{name}
