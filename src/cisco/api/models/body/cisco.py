from pydantic import AnyHttpUrl

from src.cisco.api.models.base import Base


class SourceModel(Base):
    url: AnyHttpUrl
