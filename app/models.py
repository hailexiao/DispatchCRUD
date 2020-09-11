from enum import unique
from .auth.models import User, AnonymousUser
from . import db
from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, Text, String, DateTime

class Company(db.Model):
    """
    The model for the "Company" object/table
    """

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    industry = Column(String(128), index=True)
    name = Column(String(256), index=True, unique=True)
    city = Column(String(128), index=True)
    state = Column(String(128), index=True)
    country = Column(String(128), index=True)
    phone = Column(String(128), unique=True)
    revenue = Column(BigInteger, index=True)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
