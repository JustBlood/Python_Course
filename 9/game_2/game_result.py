from dataclasses import dataclass


@dataclass
class GameResult:
    counter: int
    mistakes: int
    flag: bool
