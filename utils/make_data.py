from typing import List, Dict, Type
from random import randint
from pydantic import BaseModel

def make_data(number:int, seed_data:List[Dict], model: Type[BaseModel]):
    result = []
    index = 1
    while number:
        data = seed_data[randint(0, len(seed_data) - 1)]
        data['index'] = index
        result.append(model(**data))
        number -= 1
        index += 1
    return result
