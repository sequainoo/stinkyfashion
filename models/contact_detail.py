from models.base import Base


class ContactDetail(Base):
    """Model of Contact Detail of an individual"""
    name = "" # Name of that contact for eg 'phone'
    value = "" # for eg '0554218934'
    is_social_handle = False
    link = "" #optional
