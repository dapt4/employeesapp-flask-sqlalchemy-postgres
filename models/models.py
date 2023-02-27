from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employee'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer())
    hired_at: Mapped[int] = mapped_column(Integer())

    def __repr__(self) -> str:
        return f"Employee(id={self.id}, name={self.name}, age={self.age}), hired_at={self.hired_at}"
