import csv
import datetime

from app import models
from app.database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("sales.csv", "r") as f:
    csv_reader = csv.DictReader(f, delimiter=';')

    for row in csv_reader:
        db_record = models.Sale(
            date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            city=row["city"],
            manager=row["manager"],
            product=row["product"],
            amount=row["amount"]
        )
        db.add(db_record)

    db.commit()

db.close()