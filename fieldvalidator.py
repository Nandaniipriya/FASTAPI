from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
# now here this is schema that we are defining
class Patient(BaseModel):
  ## here we doing type validation with the help of pydantic
    
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    #   Optional module can also be used.(none is a default value)
    allergies:List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains=['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")
    
    
patient_info={'name':'John Doe','age':30,'weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@hdfc.com','phone':'123456'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)