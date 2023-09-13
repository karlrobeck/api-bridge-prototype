from pydantic import BaseModel

class PaymentGenerate(BaseModel):
    provider:str=""
    credetials:str=""