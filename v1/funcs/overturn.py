from typing import Union
from .reverse import reverse_str


def overturn_str(string: str, assemble: bool = True) -> Union[list, str]:
     words = string.split()
     overturned = list(reverse_str(words))
     if assemble:
          return " ".join(overturned)
     return overturned
