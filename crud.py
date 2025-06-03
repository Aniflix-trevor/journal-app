from sqlalchemy.orm import Session
from journalapp import models, schemas

# User CRUD
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email, password_hash="hashed_password")  # Adjust password logic as needed
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Category CRUD
def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

# JournalEntry CRUD
def create_journal_entry(db: Session, entry: schemas.JournalEntryCreate):
    db_entry = models.JournalEntry(
        title=entry.title,
        content=entry.content,
        user_id=entry.user_id,
        category_id=entry.category_id
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_journal_entries(db: Session):
    return db.query(models.JournalEntry).all()

def get_journal_entry(db: Session, entry_id: int):
    return db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()

def update_journal_entry(db: Session, entry_id: int, entry_update: schemas.JournalEntryUpdate):
    db_entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    if not db_entry:
        return None
    db_entry.title = entry_update.title
    db_entry.content = entry_update.content
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_journal_entry(db: Session, entry_id: int):
    db_entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    if not db_entry:
        return False
    db.delete(db_entry)
    db.commit()
    return True
