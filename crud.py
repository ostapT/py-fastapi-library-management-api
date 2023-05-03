from sqlalchemy.orm import Session

import models
import schemas
from models import DBAuthor


def get_all_authors(db: Session,  skip: int = 0, limit: int = 10):
    return db.query(DBAuthor).offset(skip).limit(limit).all()


def get_author_by_name(db: Session, name: str):
    return (
        db.query(models.DBAuthor).filter(models.DBAuthor.name == name).first()
    )


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author_by_id(db: Session, author_id: int):
    return (
        db.query(models.DBAuthor)
        .filter(models.DBAuthor.id == author_id).first()
    )


def get_all_books(
        db: Session,
        author_id: int | None = None,
        skip: int = 0,
        limit: int = 10
):
    queryset = db.query(models.DBBook)

    if author_id is not None:
        queryset = queryset.filter(models.DBBook.author_id == author_id)

    return queryset.offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return (
        db.query(models.DBBook).filter(models.DBBook.id == book_id).first()
    )


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.DBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def get_book_by_title(db: Session, title: str):
    return (
        db.query(models.DBBook).filter(models.DBBook.title == title).first()
    )