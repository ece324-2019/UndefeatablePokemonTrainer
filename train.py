import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from read_pokedex import get_data
from dataset import TurnDataset
from torch.utils.data import DataLoader
from models import MultiLayerPerceptron
import argparse

import read_pokedex

def plot_over_acc(over_acc, steps):
    plt.figure()
    plt.plot(steps, over_acc)
    plt.title('Overfit Accuracy vs. Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.show()
def plot_over_loss(over_loss, steps):
    plt.figure()
    plt.plot(steps, over_loss)
    plt.title('Overfit Loss vs. Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()
def find_acc(pred, labels):
    running_pred = 0.0
    for i in range(len(pred)):
        if torch.argmax(pred[i]) == torch.argmax(labels[i]):
            running_pred += 1
    return running_pred



parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', type=int, default=995)
parser.add_argument('--lr', type=float, default=0.1)
parser.add_argument('--epochs', type=int, default=200)
parser.add_argument('--input_size', type=int, default=43)
parser.add_argument('--hidden_dim', type=int, default=20)
parser.add_argument('--output_size', type=int, default=4)
parser.add_argument('--num_filt', type=int, default=50)

args = parser.parse_args()

def get_model():

    # Load the data

    training_data, training_labels = get_data()
    train_dataset = TurnDataset(training_data, training_labels)
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)

    model = MultiLayerPerceptron(args.input_size, args.hidden_dim, args.output_size)
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=args.lr)

    train_loss = []
    train_acc = []

    steps = [i for i in range(args.epochs)]
    sig = nn.Sigmoid()

    for epoch in range(args.epochs):
        running_loss = 0.0
        running_acc = 0.0
        running_count = 0.0
        for i, batch in enumerate(train_loader, 0):
            feats, labels = batch
            optimizer.zero_grad()
            outputs = model(feats.float())
            loss = criterion(input=outputs.squeeze(), target=labels.float())
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            running_acc += find_acc(outputs, labels)
            running_count += len(labels)
        train_loss.append(running_loss)
        train_acc.append(running_acc/running_count)
    print('Finished Training')
    # plot_over_acc(train_acc, steps)
    # plot_over_loss(train_loss, steps)
    return model

if __name__ == "__main__":
    model = get_model()
    pokedex = read_pokedex.get_dataframe()
    input = torch.from_numpy(read_pokedex.inputize_data(pokedex.loc[pokedex['species'] == 'Haxorus'].index.values[0]))
    print ("input", input)
    move = model(input.float())
    print(move)
    moves = ['1', '2', '3', '4']
    print(moves[torch.argmax(model(input.float()))])