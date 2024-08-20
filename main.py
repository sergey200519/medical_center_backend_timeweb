from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Timeweb Cloud + FastAPI = ❤️"



if __name__ == "__main__":
    uvicorn.run(app, port=80)
