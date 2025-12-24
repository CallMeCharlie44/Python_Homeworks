import pytest
from models_SQL import Student, Base, engine, SessionLocal


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_add_student(db_session):
    student = Student(name="Ivan", age=20)
    db_session.add(student)
    db_session.commit()

    saved = db_session.query(Student).filter_by(name="Ivan").first()
    assert saved is not None
    assert saved.age == 20


def test_update_student(db_session):
    student = Student(name="Anna", age=22)
    db_session.add(student)
    db_session.commit()

    student.age = 23
    db_session.commit()

    updated = db_session.query(Student).filter_by(name="Anna").first()
    assert updated.age == 23


def test_delete_student(db_session):
    student = Student(name="Petr", age=25)
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

