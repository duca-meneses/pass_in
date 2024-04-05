from sqlalchemy.exc import IntegrityError

from pass_in.models.settings.connection import db_connection_handler
from pass_in.models.entities.check_ins import CheckIns
from pass_in.errors.error_types.http_conflict import HttpConflictError


class CheckInRepository:

    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:    
            try:
                check_in =(
                    CheckIns(attendeeId=attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            except IntegrityError:
                raise HttpConflictError('Check In ja cadastrado!')
            except Exception as exception:
                database.session.rollback()
                raise exception