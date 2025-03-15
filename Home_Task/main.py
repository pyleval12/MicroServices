from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message":"Hello from Flask!"}
# if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# uvicorn main:app --reload