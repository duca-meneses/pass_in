import uuid

from pass_in.http_types.http_request import HttpRequest
from pass_in.http_types.http_response import HttpResponse
from pass_in.models.repository.events_repository import EventsRepository


class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body['uuid'] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body={ 'eventId': body['uuid'] },
            status_code=201
        )