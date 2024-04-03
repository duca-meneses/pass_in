from fastapi import APIRouter, status

event_router = APIRouter(prefix='/api', tags=['events'])

@event_router.post('/events', status_code=status.HTTP_201_CREATED)
def create_event():
    return { 'Olá': 'Mundo' }