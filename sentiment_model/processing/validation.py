from typing import List

from pydantic import BaseModel, ValidationError


class TextInput(BaseModel):
    text: str


class TextsInput(BaseModel):
    texts: List[TextInput]


def validate_inputs(input_data):
    try:
        TextsInput(**input_data)
        return True, None
    except ValidationError as e:
        return False, e.errors()
