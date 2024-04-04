import pytest

from pass_in.models.repository.attendees_repository import AttendeesRepository
from pass_in.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registo no banco de dados')
def test_insert_attendee():
    event_id = '9ac406e4-8205-4e54-abe6-7106b4a9a420'
    attendee_info = {
        'uuid': 'meu-uuid-test-api',
        'name': 'attendee',
        'email': 'mail@example.com',
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
    
