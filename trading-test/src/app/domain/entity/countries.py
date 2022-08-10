from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from enum import Enum

@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass(frozen=True)
class Conutry(Enum):
    SWEDEN = "sweden"
    MEXICO = "mexico"
    THAILAND = "thailand"
    BRAZIL = "brazil"
    

    @staticmethod
    def from_str(label):
        if label in ('mexico'):
            return Conutry.MEXICO
        if label in ('sweden'):
            return Conutry.SWEDEN
        if label in ('thailand'):
            return Conutry.THAILAND
        else:
            msg = "provider with name {NAME} was not found".format(NAME=label)
            raise Exception(msg)
