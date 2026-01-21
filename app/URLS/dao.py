from app.URLS.models import URLsModel
from app.dao.base import BaseDao


class LinkDao(BaseDao):
    model = URLsModel