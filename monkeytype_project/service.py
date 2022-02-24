from flask import Flask
from models import db, EmployeeModel
from typing import Dict, List, Union




class Employee:

    def create(self, payload: Dict[str, Union[str, int]]) -> Union[bool, EmployeeModel]:
        try:
            employee = EmployeeModel(payload.get("name"), payload.get("age"), payload.get("position"))
            db.session.add(employee)
            db.session.commit() 
            return employee
        except:
            return False
    
    def get_all(self) -> List[Dict[str, Union[str, int]]]:
        employe_list =  EmployeeModel.query.all()
        employe_list = [e.as_dict() for e in employe_list]
        return employe_list