class Question:
    """Models a question."""

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"Text: {self.text}, answer: {self.answer}"
