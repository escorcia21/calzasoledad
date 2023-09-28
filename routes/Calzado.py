from typing import Optional
from flask import Blueprint
from services.CalzadoService import CalzadoService


bp = Blueprint('calzado', __name__, url_prefix='/calzado')

@bp.route("/", methods=['GET'])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    calzadoService: CalzadoService = CalzadoService()
):

    return [
        calzado.__repr__()
        for calzado in calzadoService.list(
            name, pageSize, startIndex
        )
    ]
