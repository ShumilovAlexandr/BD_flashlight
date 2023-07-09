from pydantic import BaseModel
from typing import Optional

from utils import CommandChoice


class Form(BaseModel):
    command: CommandChoice
    metadata: Optional[str]

