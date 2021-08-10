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
                pass
            else:
                break
        else:
            break
        if winner := game.detect_winner():
            break
    return winner, game


def train() -> NeuralNetwork:
    population = [NeuralNetwork(100, [20, 10]) for _ in range(10)]
    for i in range(50):
        print(f"Generation {i}")
        scores = []
        for nn0 in population:
            score = 0
            for nn1 in population:
                if nn0 is nn1:
                    continue
                if play(nn0, nn1)[0] == 1:
                    score += 1
            scores.append(score)
        best = population[np.argmax(scores)]
        population = [best.clone() for _ in range(len(population))]
        for nn in population:
            if nn is not best:
                nn.mutate()
    return best


def play_against_computer():
    computer = train()
    game = Connect4()
    while True:
        col = int(input("Choose col"))
        game.play(col)
        state = np.array(game.grid).flatten()
        moves = computer.feedforward(state).argsort()
        for move in moves:
            try:
                game.play(move)
            except IllegalMove:
                pass
            else:
                break
        else:
            print("Computer cannot play")
            break
        print(game)
        if player := game.detect_winner():
            print(f"Winner is {player}")
            break


if __name__ == '__main__':
    player0 = NeuralNetwork(100, [20, 10])
    player1 = train()
    for i in range(10):
        winner, game = play(NeuralNetwork(100, [20, 10]), player1)
        print(game)
        print(winner)

