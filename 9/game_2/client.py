from game_result import GameResult
from game import Game
from game_status import GameStatus

def end_of_game_handler(result: GameResult):
    print(f"Questions asked:{result.counter}, Mistakes made:{result.mistakes}.")
    print("You won!" if result.flag else "You lost!")


game = Game("E:\prog_py\Course_py\9. Движемся дальше\Questions.csv", end_of_game_handler, max_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n'")
    print(q.text)

    answer = input() == "y"
    if q.is_correct == answer:
        print("Good job! You're right!")
    else:
        print("Oops, actually you're mistaken. Here is the explanation: ")
        print(q.explanation)

    game.give_answer(answer)