from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text


from  datetime import  datetime

from contact import Contact

database = r"D:\Web_Development\kill_enemy\circle\circle_v1\src\db\circle.db"
Base = declarative_base()

# engine = create_async_engine(database, echo=True)
# AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Reminder(Base):

    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    title = Column(String, nullable=False)
    message = Column(Text)
    remind_at = Column(DateTime, nullable=False)
    repeat = Column(String, default="once")  # once, yearly, monthly, weekly, etc.
    status = Column(String, default="pending")  # pending, sent, skipped
    channel = Column(String, default="desktop")  # desktop, sms, email
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship: many reminders belong to one contact
    contact = relationship("Contact", back_populates="reminders")
