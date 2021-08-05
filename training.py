import numpy as np

from env import Connect4, IllegalMove
from neural_network import NeuralNetwork


def play(nn1: NeuralNetwork, nn2: NeuralNetwork):
    game = Connect4()
    winner = 0
    for i in range(100):
        player = nn1 if i % 2 == 0 else nn2
        state = np.array(game.grid).flatten()
        moves = player.feedforward(state).argsort()
        for move in moves:
            try:
                game.play(move)
            except IllegalMove:
                print("First choice impossible")
            else:
                break
        else:
            break
        if winner := game.detect_winner():
            break
    return winner, game


if __name__ == '__main__':
    winner, game = play(NeuralNetwork(100, [20, 10]), NeuralNetwork(100, [20, 10]))
    print(winner)
    print(game)
