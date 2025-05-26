from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import requests
from app import models, schemas, crud
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Service Monitor API", version="0.1.0")

#CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 👈 React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Health check route
@app.get("/")
def root():
    return {"message": "Service Monitor API is running"}

# 🔹 POST /status — Add a new service status
@app.post("/status/", response_model=schemas.Status)
def create_status(status: schemas.StatusCreate, db: Session = Depends(get_db)):
    return crud.create_status(db=db, status=status)

# 🔹 GET /status — Get all service statuses
@app.get("/status/", response_model=list[schemas.Status])
def read_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_statuses(db, skip=skip, limit=limit)

#external_API
@app.get("/external_users/")
def external_users():
    try:
        response = requests.get("https://fake-json-api.mock.beeceptor.com/users")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/TEST1/")
def external_users():
    try:
        response = requests.get("https://www.srilankan.com/")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    