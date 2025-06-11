from app import app, db
from models import User, Job

with app.app_context():
    # Add HR user
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", password="admin123")
        db.session.add(admin)

    # Add sample jobs
    if Job.query.count() == 0:
        job1 = Job(title="Site Reliability Engineer", description="Maintain infrastructure reliability.")
        job2 = Job(title="DevOps Engineer", description="Automate deployments and manage CI/CD pipelines.")
        job3 = Job(title="Python Developer", description="Build backend services using Flask and Django.")
        db.session.add_all([job1, job2, job3])

    db.session.commit()
    print("✅ Seed data inserted.")
