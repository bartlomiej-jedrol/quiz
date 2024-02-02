class QuizBrain:
    """Models the QuizBrain quiz."""

    def __init__(self, question_list: list["Question"]) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Serves next question from the question bank."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        ).lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks the user answer against the correct answer."""
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_questions(self):
        """Returns if the quiz still has questions."""
        return self.question_number < len(self.question_list)
