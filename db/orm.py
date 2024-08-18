from sqlalchemy.orm import Session
from db import models



def read_reviews(db: Session):
    return db.query(models.Reviews).all()

def read_reviews_by_id(db: Session, id: int):
    return db.query(models.Review).filter(models.Review.id == id).first()

def create_review(db: Session, review: dict):
    new_review = models.Reviews(**review)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review