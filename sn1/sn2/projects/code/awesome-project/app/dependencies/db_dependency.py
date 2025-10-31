from sqlmodel import SQLModel, Session, create_engine


DATABASE_URL = "sqlite:///./test.db"
enginer = create_enginer(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        tield session
