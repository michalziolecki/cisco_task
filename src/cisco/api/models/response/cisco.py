from typing import Union, Dict, List

from src.cisco.api.models.base import Base


class InfoModel(Base):
    receiver: str = "Cisco is the best !"


class PingModel(Base):
    payload: Union[Dict, List, str]
