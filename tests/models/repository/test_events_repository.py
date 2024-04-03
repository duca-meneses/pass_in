import pytest

from pass_in.models.repository.events_repository import EventsRepository
from pass_in.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_event():
    event = {
        'uuid': 'uuid-e-nois',
        'title': 'test title',
        'slug': 'test-slug',
        'maximum_attendees': 20
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="teste realizado com sucesso")
def test_get_event_id():
    event_id = 'uuid-e-nois'
    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(event_id)
    print(response)
    print(response.title)
        