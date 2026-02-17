import numpy as np
import torch
from torch.utils.data import Dataset


def random_density_matrix(dim=4):
    A = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)
    rho = A @ A.conj().T
    rho = rho / np.trace(rho)
    return rho


def density_to_L(rho):
    return np.linalg.cholesky(rho)


def pauli_measurements(rho):
    Z = np.array([[1, 0], [0, -1]])
    I = np.eye(2)

    ops = [
        np.kron(Z, Z),
        np.kron(Z, I),
        np.kron(I, Z)
    ]

    measurements = []
    for O in ops:
        measurements.append(np.real(np.trace(rho @ O)))

    return np.array(measurements, dtype=np.float32)


class DensityMatrixDataset(Dataset):
    def __init__(self, n_samples=1000):
        self.inputs = []
        self.targets = []

        for _ in range(n_samples):
            rho = random_density_matrix()
            L = density_to_L(rho)

            x = pauli_measurements(rho)
            y = L.flatten().real

            self.inputs.append(x)
            self.targets.append(y)

        self.inputs = torch.tensor(self.inputs,dtype=torch.float32)
        self.targets = torch.tensor(self.targets,dtype=torch.float32)

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        return self.inputs[idx], self.targets[idx]
