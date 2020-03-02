#!/usr/bin/env python
# -*- codding: utf-8 -*- 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine

Base = declarative_base()

class FundBasic(Base):
    __tablename__ = 'fund_basic'
    id = Column(Integer, primary_key=True, auto_increment=True)
    code = Column(String(8), nullable=False)
    name = Column(String(32), nullable=False)
    type_name = Column(String(16))
    pinyin_name = Column(String(64))
    pinyin_brief = Column(String(16))


if __name__ == '__main__':
    engine = create_engine('sqlite:///fund.db')
    Base.metadata.create_all(engine)