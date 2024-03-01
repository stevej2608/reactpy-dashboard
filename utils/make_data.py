from typing import List, Dict, Type, Any, TypeVar, cast
from random import randint
from pydantic import BaseModel

DataModel = TypeVar('DataModel', bound=BaseModel)

def make_data(number:int, seed_data:List[Dict[str, Any]], model: Type[DataModel])-> List[DataModel]:
    result: List[DataModel] = []
    index = 1
    while number:
        data = seed_data[randint(0, len(seed_data) - 1)]
        data['index'] = index
        result.append(model(**cast(Any, data)))
        number -= 1
        index += 1
    return result
