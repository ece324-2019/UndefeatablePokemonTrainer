import torch.nn as nn
import torch.nn.functional as F
import torch

class MultiLayerPerceptron(nn.Module):
	def __init__(self, input_size, hidden_size, output_size):
		super(MultiLayerPerceptron, self).__init__()
		self.fc1 = nn.Linear(input_size, hidden_size)
		self.fc2 = nn.Linear(hidden_size, output_size)
	def forward(self, features):
		x = self.fc1(features)
		x = self.fc2(x)
		return x

