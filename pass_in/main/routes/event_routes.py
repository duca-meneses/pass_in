from flask import Blueprint, request, jsonify

from pass_in.data.event_handler import EventHandler
from pass_in.http_types.http_request import HttpRequest

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def create_event():
    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()

    http_response = event_handler.register(http_request)
    return jsonify(http_response.body), http_response.status_code