import torch
import scipy.linalg
import numpy as np

def quantum_fidelity(rho, sigma):
    rho = rho.detach().cpu().numpy()
    sigma = sigma.detach().cpu().numpy()

    sqrt_rho = scipy.linalg.sqrtm(rho)
    product = sqrt_rho @ sigma @ sqrt_rho
    sqrt_product = scipy.linalg.sqrtm(product)

    fidelity = (np.trace(sqrt_product).real) ** 2
    return fidelity


def trace_distance(rho, sigma):
    diff = rho - sigma
    eigvals = torch.linalg.eigvals(diff)
    return 0.5 * torch.sum(torch.abs(eigvals)).item()
