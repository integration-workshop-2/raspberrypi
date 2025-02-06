from typing import NamedTuple, Optional


class MAX30102Response(NamedTuple):
    bpm: Optional[int] = None
    oxygenation_percentage: Optional[float] = None
