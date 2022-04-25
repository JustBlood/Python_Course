from dataclasses import dataclass


@dataclass
class Question:
    text: str
    is_correct: bool
    explanation: str
