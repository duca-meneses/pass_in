import pytest

from pass_in.models.repository.attendees_repository import AttendeesRepository
from pass_in.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registo no banco de dados')
def test_insert_attendee():
    event_id = 'uuid-e-nois'
    attendee_info = {
        'uuid': 'meu_uuid',
        'name': 'attendee',
        'email': 'email@example.com',
        'event_id': event_id,
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee_info)
    print(response)

@pytest.mark.skip(reason='test realizado com sucesso')
def test_get_attendee_badge_by_id():
    attendee_id = 'meu_uuid'
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)
    
