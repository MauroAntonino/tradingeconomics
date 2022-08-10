from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from typing import List

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass(frozen=False, init=True)
class Data:
    label: List
    value: List