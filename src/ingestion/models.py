from dataclasses import dataclass
from typing import List , Optional

@dataclass
class AIUpdate:
    title : str
    source : str
    url : str
    date : str
    category : str
    summary : Optional[str] = None
    tags : Optional[List[str]] = None


