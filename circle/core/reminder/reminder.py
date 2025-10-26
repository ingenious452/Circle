# SQLAlchemy model
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from circle.core.orm.database import Base

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    message = Column(String, nullable=False)
    remind_at = Column(DateTime, nullable=True)  # for one-time or next occurrence
    recurrence = Column(JSON, nullable=True)    # {"type":"daily"} or {"type":"weekly", "day_of_week":1}
    channels = Column(JSON, nullable=False)    # ["desktop", "email"]
    notified = Column(Boolean, default=False)
