from flask_sqlalchemy import SQLAlchemy
from typing import Dict, Union
 
db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "employe"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
 
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position
 
    def __repr__(self):
        return f"{self.name}:{self.id}"
    
    def as_dict(self) -> Dict[str, Union[str, int]]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    