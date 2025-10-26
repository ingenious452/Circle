from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import declarative_base, relationship

from datetime import datetime


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True)
    email = Column(String, unique=True, nullable=True)
    birthday = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)

    reminders = relationship("Reminder", back_populates="contact", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Contact(name={self.name}>"




