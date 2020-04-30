from game_files.game import Game

game = Game()
while True:
    game.board.show_state()
    x = input("w - up, a - left, d - right, s - down: ")
    if not game.next(x):
        break