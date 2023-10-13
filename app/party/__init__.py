from flask import Blueprint

bp = Blueprint('party', __name__, template_folder='templates')

from app.party import routes