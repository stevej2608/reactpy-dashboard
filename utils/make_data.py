from typing import List, Dict
from random import randint
from pydantic import BaseModel

def make_data(number:int, seed_data:List[Dict], model:BaseModel):
    result = []
    while number:
        data = seed_data[randint(0, len(seed_data) - 1)]
        result.append(model(**data))
        number -= 1
    return result
