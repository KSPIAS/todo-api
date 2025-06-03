from database import SessionLocal
from sqlalchemy import text

def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("✅ Connected to database successfully.")
    except Exception as e:
        print("❌ Failed to connect to database.")
        print("Error:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
