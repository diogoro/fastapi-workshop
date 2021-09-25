"""
fastapi_workshop base module.
"""
from fastapi import FastAPI, Depends
from .db import init_db, engine, Session, get_session
from .model.user import User, UserIn, UserOut, UserList
app = FastAPI(
    title='API de Usuarios do Diogo',
    version='0.0.1',
    on_startup=[init_db]
)


@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/user", response_model=UserList)
def list_user(session: Session = Depends(get_session)):
    return session.query(User).all()

@app.post("/user", response_model=UserOut)
def create_user(user: UserIn, session: Session = Depends(get_session)):
    user_ = User.from_orm(user)
    session.add(user_)
    session.commit()
    session.refresh(user_)
    return user_

@app.delete("/user/{userid}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    session.delete(user)
    session.commit()
    return {"message": "Deleted user"}