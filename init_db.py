from db.models import Base
from db.session import engine

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
