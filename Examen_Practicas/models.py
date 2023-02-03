from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
   
   #Table Model
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=True)
    username = fields.CharField(max_length=20, unique=True)
    
    
User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
