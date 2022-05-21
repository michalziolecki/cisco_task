from pydantic import BaseModel


class Base(BaseModel):
    ...


class HomeModel(Base):
    info: str = "Welcome in the Cisco task. To read documentation go to '/docs'"
