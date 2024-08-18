import json
from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
import uvicorn

from db import models
from db.models import Reviews
from db.orm import read_reviews, read_reviews_by_id, create_review
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def from_modal_to_json(modal, headers):
    res = []
    for item in modal:
        item_dict = {}
        for it in headers:
            item_dict[it] = item[it]
        res.append(item_dict)
    return res
     


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return "hi"

@app.get("/reviews/")
def get_reviews(db: Session = Depends(get_db)):
    answer = db.query(models.Reviews).all()
    # print(answer, answer[0], dir(answer[0]), jsonable_encoder(answer))
    # return answer
    return jsonable_encoder(answer)
    # return read_reviews(db:Session=Depends(get_db))


@app.api_route('/reviews/', methods=['POST'])
def create_reviews(review: dict, db: Session = Depends(get_db)):
    create_review(db, review)
    answer = db.query(models.Reviews).all()
    return jsonable_encoder(answer)


if __name__ == "__main__":
    uvicorn.run(app, port=10000)