from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.db import models  # noqa: F401