from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db.db_config import Base

class Student(Base):
    __tablename__ = "student"

    s_id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    s_name:Mapped[str] = mapped_column(String(100), nullable=False)
    s_age:Mapped[int] = mapped_column(Integer, nullable=False)
    s_marks:Mapped[int] = mapped_column(Integer, nullable=False)