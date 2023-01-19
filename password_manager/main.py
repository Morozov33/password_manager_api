from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select, delete
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from password_manager.database import engine, get_session, create_tables
from password_manager.model import (Passwords, PasswordRead,
                                    PasswordCreateUpdate)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_tables()


@app.on_event("shutdown")
def on_shutdown():
    pass
    # Clear DB when app is shutdown
    # with Session(engine) as session:
    #     session.exec(delete(Passwords))
    #     session.commit()


@app.get("/")
def root():

    # Welcome message from root
    return {
        "message": (
            """Hello, everyone!\
 It's simple password manager for everyone. Let's use it!"""
        )
    }


@app.get("/password/{service_name}", response_model=PasswordRead)
def read_password(
        *,
        session: Session = Depends(get_session),
        service_name: str,
):
    try:
        password_db = session.exec(
                select(Passwords).where(Passwords.service_name == service_name)
        ).one()
    except NoResultFound:
        raise HTTPException(
                status_code=404,
                detail="Password not found",
        )
    else:
        return password_db


@app.get("/password")
def read_part_of_service_name(
        *,
        session: Session = Depends(get_session),
        service_name: str,
):
    if not service_name:
        raise HTTPException(
                status_code=400,
                detail="Invalid value for service_name",
        )
    password_db = session.exec(
            select(Passwords).where(
                Passwords.service_name.ilike(
                    f"%{service_name}%"
                )
            )
    ).all()

    if not password_db:
        raise HTTPException(
                status_code=404,
                detail="Services not found",
        )

    return password_db


@app.post("/password/{service_name}", response_model=PasswordRead)
def create_update_password(
        *,
        session: Session = Depends(get_session),
        password_model: PasswordCreateUpdate,
        service_name: str,
):

    db_password = session.exec(
            select(Passwords).where(
                Passwords.service_name == service_name)).first()

    if not db_password:
        db_password = Passwords.from_orm(password_model)
        db_password.service_name = service_name
        session.add(db_password)
        session.commit()
        session.refresh(db_password)

    else:
        password_data = password_model.dict(exclude_unset=True)

        for key, value in password_data.items():
            setattr(db_password, key, value)
        session.add(db_password)
        session.commit()
        session.refresh(db_password)

    return db_password


@app.delete("/password/{service_name}")
def delete_password(
        *,
        session: Session = Depends(get_session),
        service_name: str,
):
    db_password = session.exec(select(Passwords).where(Passwords.service_name == service_name)).one()

    if not db_password:
        raise HTTPException(
                status_code=404,
                detail="Password not found",
        )

    session.delete(db_password)
    session.commit()

    return {"ok": True}
