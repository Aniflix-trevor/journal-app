from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, DeclarativeBase
from datetime import datetime
# from database import Base

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    journal_entries = relationship('JournalEntry', back_populates='user', cascade='all, delete-orphan')

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    
    journal_entries = relationship('JournalEntry', back_populates='category', cascade='all, delete-orphan')

class JournalEntry(Base):
    __tablename__ = 'journal_entries'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    title = Column(String(255), nullable=False)  # Added title column
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship('User', back_populates='journal_entries')
    category = relationship('Category', back_populates='journal_entries')
