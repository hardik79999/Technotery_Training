from app import app
from extensions import db
from models import User, Task
from werkzeug.security import generate_password_hash
from faker import Faker
import random

# create faker object
fake = Faker()

def seed_database():

    with app.app_context():
        print("🌱 Planting seeds... wait")

        hashed_password = generate_password_hash('123')


        admin = User.query.filter_by(email='admin@test.com').first()
        if not admin:
            admin = User(role='admin', username='superuser', email='admin@test.com', password=hashed_password)
            db.session.add(admin)
            db.session.commit()
            print("Admin account created!")

        # create fake manager
        users_list = []

        print("Creating 3 Managers & 7 Employees...")

        for _ in range(3):
            manager = User(role='manager', username=fake.user_name(),email=fake.email(), password=hashed_password, created_by=admin.id)
            db.session.add(manager)
            users_list.append(manager)

        for _ in range(7):
            employee = User(role='employee', username=fake.user_name(), email=fake.email(),password=hashed_password, created_by=admin.id)
            db.session.add(employee)
            users_list.append(employee)

        db.session.commit()

        print("Generating 15 random Tasks...")

        employees = User.query.filter_by(role='employee').all()
        managers = User.query.filter_by(role='manager').all()

        for _ in range(15):
            task = Task(
                title = fake.sentence(nb_words=4),
                description = fake.text(),
                status = random.choice(['pending', 'in progress', 'completed']),
                assigned_to =random.choice(employees).id, # assigned random employee
                assigned_by = random.choice(managers).id # assigned_by any manager
            )
        db.session.commit()
        print("seeded create successfully....")

if __name__ == '__main__':
    seed_database()