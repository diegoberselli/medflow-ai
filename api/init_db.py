from database import engine, Base, SessionLocal, Patient, Doctor, Schedule
from datetime import datetime, timedelta

def create_tables():
    Base.metadata.create_all(bind=engine)

def populate_data():
    db = SessionLocal()

    patients = [
        Patient(name="João Silva", email="joao@email.com", phone="11999999999"),
        Patient(name="Maria Santos", email="maria@email.com", phone="11888888888"),
        Patient(name="Pedro Costa", email="pedro@email.com", phone="11777777777")
    ]

    doctors = [
        Doctor(name="Dr. Carlos Lima", specialty="Cardiologia", price=200.0),
        Doctor(name="Dra. Ana Souza", specialty="Dermatologia", price=150.0),
        Doctor(name="Dr. Paulo Rocha", specialty="Clínico Geral", price=120.0)
    ]

    base_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    
    schedules = [
        Schedule(
            doctor_id=doctor_id,
            datetime=base_date + timedelta(days=day, hours=hour - 9),
            available=True
        )
        for day in range(7)
        for hour in [9, 10, 11, 14, 15, 16]
        for doctor_id in [1, 2, 3]
    ]

    db.add_all(patients + doctors + schedules)
    db.commit()
    db.close()

if __name__ == "__main__":
    create_tables()
    populate_data()
    print("Banco de dados criado e populado com sucesso!")
