from app.presenca.controllers import PresencaCreate, PresencaDetails
from flask import Blueprint




presenca_api = Blueprint ('presenca_api', __name__)

presenca_api.add_url_rule(

    '/presenca/create', view_func=PresencaCreate.as_view('presenca_create'), methods = ['GET', 'POST']

)
presenca_api.add_url_rule(

    '/presenca/details/<int:id>', view_func=PresencaDetails.as_view('presenca_details'), methods = ['GET', 'PUT', 'PATCH', 'DELETE']

)