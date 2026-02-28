from .app import settings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session



engine = create_engine(settings.sync_url, future=True)
Sessionmaker = sessionmaker(bind=engine)

def seed_data(session: Session, file_path: str = "test_data.sql"):
    exists = session.execute(text("SELECT 1 FROM organizations LIMIT 1")).fetchone()

    if not exists:
        print(f"Загрузка тестовых данных из {file_path}...")
        with open(file_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
            session.execute(text(sql_script))
            session.commit()
        print("Данные успешно загружены.")
    else:
        print("База уже содержит данные, пропускаю заполнение.")