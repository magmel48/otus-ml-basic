from typing import Any
from pydantic import BaseModel
from metadata import Metadata


class File(BaseModel):
    content: Any
    "Cannot be a particular type, because open() returns str, wave returns Wave_read/Wave_write object, etc."

    metadata: Metadata
