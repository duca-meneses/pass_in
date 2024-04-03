from pass_in.models.settings.base import Base
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = 'check_ins'

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey('attendees.id'))
    def __repr__(self):
        return f'CheckIns [attendeeId={self.attendeeId}]'