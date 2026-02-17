import torch
import torch.nn as nn

class DensityNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 16)
        )

    def forward(self, x):
        return self.net(x)
