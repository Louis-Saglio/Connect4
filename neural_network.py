from __future__ import annotations

import random
from typing import Iterable

import numpy as np


def sigmoid(array):
    return 1/(1+np.exp(-array))


def relu(array):
    return np.maximum(0, array)


class NeuralNetwork:
    def __init__(self, input_size: int, layers_size: Iterable[int]):
        self.layers = []
        for layer_size in layers_size:
            self.layers.append(
                {
                    "weights": np.random.random((layer_size, input_size)),
                    "bias": np.random.random(layer_size),
                    "activation": relu,
                }
            )
            input_size = layer_size

    def feedforward(self, input_data) -> np.ndarray:
        for layer in self.layers:
            input_data = np.dot(layer["weights"], input_data) + layer["bias"]
            input_data = layer["activation"](input_data)
        return input_data / np.sum(input_data)

    def clone(self) -> NeuralNetwork:
        new = NeuralNetwork(0, [])
        for layer in self.layers:
            new.layers.append(
                {
                    "weights": layer["weights"].copy(),
                    "bias": layer["bias"].copy(),
                    "activation": layer["activation"],
                }
            )
        return new

    def mutate(self):
        layer = random.choice(range(0, len(self.layers)))
        neuron = random.choice(range(0, len(self.layers[layer]["weights"])))
        weight = random.choice(range(0, len(self.layers[layer]["weights"][neuron])))
        self.layers[layer]["weights"][neuron][weight] += (random.random() - 0.5) * 10


if __name__ == '__main__':
    nn = NeuralNetwork(input_size=100, layers_size=[50, 25, 10])
    data = np.random.random(100)
    clone = nn.clone()
    nn.mutate()
