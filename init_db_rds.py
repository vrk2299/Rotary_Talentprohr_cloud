# init_db_rds.py
from app import db, app

with app.app_context():
    db.create_all()
    print("✅ RDS tables created safely.")
