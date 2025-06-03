from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from journalapp import models, database, schemas, crud  # adjust import paths to your project
from journalapp.database import SessionLocal, engine

# Create the tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# CORS settings (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User endpoints
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Category endpoints
@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

# Journal entry endpoints
@app.post("/journal_entries/", response_model=schemas.JournalEntry)
def create_journal_entry(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    return crud.create_journal_entry(db, entry)

@app.get("/journal_entries/", response_model=list[schemas.JournalEntry])
def read_journal_entries(db: Session = Depends(get_db)):
    return crud.get_journal_entries(db)

@app.put("/journal_entries/{entry_id}", response_model=schemas.JournalEntry)
def update_journal_entry(entry_id: int, entry_update: schemas.JournalEntryUpdate, db: Session = Depends(get_db)):
    updated_entry = crud.update_journal_entry(db, entry_id, entry_update)
    if updated_entry:
        return updated_entry
    raise HTTPException(status_code=404, detail="Entry not found")

@app.delete("/journal_entries/{entry_id}")
def delete_journal_entry(entry_id: int, db: Session = Depends(get_db)):
    success = crud.delete_journal_entry(db, entry_id)
    if success:
        return {"message": "Entry deleted successfully"}
    raise HTTPException(status_code=404, detail="Entry not found")
