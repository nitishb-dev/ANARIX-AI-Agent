from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SalesMetrics(Base):
    __tablename__ = "sales_metrics"
    id = Column(Integer, primary_key=True)
    product_name = Column(String(255))
    sales_value = Column(Float)

class Eligibility(Base):
    __tablename__ = "eligibility"
    id = Column(Integer, primary_key=True)
    customer_id = Column(String(50))
    eligible = Column(String(10))

class TotalSalesMetrics(Base):
    __tablename__ = "total_sales_metrics"
    id = Column(Integer, primary_key=True)
    region = Column(String(100))
    total_sales = Column(Float)
