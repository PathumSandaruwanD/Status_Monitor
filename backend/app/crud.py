from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_status(db: Session, status: schemas.StatusCreate):
    db_status = models.ServiceStatus(
        service_name=status.service_name,
        status=status.status,
        timestamp=datetime.utcnow()
    )
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_all_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ServiceStatus).offset(skip).limit(limit).all()
