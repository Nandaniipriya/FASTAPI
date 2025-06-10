from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
# now here this is schema that we are defining
class Patient(BaseModel):
  ## here we doing type validation with the help of pydantic
    
    name:Annotated[str,Field(min_length=50,title="Name of the patient",description='Give the name of the patient in less than 50 chars',examples=['Nitish','Amit'])]
    email:EmailStr
    age:int
    weight:float=Field(gt=0)
    married:bool
    #   Optional module can also be used.(none is a default value)
    allergies:Optional[List[str]]=None
    contact_details: Dict[str, str]
    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")
    
    
patient_info={'name':'John Doe','age':30,'weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'123456'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)