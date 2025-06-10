from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin:str
    
class Patient(BaseModel):
    name: str
    age: int
    gender:str
    address: Address
    
address_dict={'city':'gurgaon','state':'haryana','pin':'122018'}
address1=Address(**address_dict)
patient_dict={'name':'nitish','age':35,'address':address1,'gender':'male'}
patient1 = Patient(**patient_dict)
temp=patient1.model_dump()

print(temp)
print(type(temp))