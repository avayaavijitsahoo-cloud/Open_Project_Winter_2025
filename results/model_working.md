# Model Working and Methodology

## Overview
This project reconstructs a valid quantum density matrix from measurement data using a
physics-informed machine learning approach. Instead of directly predicting the density
matrix, the model predicts a lower-triangular matrix L and reconstructs the density matrix
as ρ = LL† / Tr(LL†), ensuring physical validity by construction.
---

## Density Matrix Constraints
A physical density matrix ρ must satisfy:
1. Hermiticity: ρ = ρ†
2. Positive semi-definiteness: eigenvalues ≥ 0
3. Unit trace: Tr(ρ) = 1
Direct prediction of ρ using neural networks does not guarantee these properties.
---

## Cholesky-Based Parameterization
To enforce physical constraints, we use a Cholesky decomposition:
ρ = LL†

The neural network predicts the elements of a lower-triangular matrix L. The reconstructed
density matrix is normalized by its trace:
ρ = LL† / Tr(LL†)

This guarantees:
- Positive semi-definiteness
- Hermiticity
- Unit trace

This technique is widely used in quantum state tomography and constrained optimization.
---

## Input Representation
The input to the model consists of expectation values of Pauli observables:
⟨Z ⊗ Z⟩, ⟨Z ⊗ I⟩, and ⟨I ⊗ Z⟩

These measurements form a compact representation of classical shadow data for a
two-qubit quantum system.
---

## Neural Network Architecture
The model is a fully connected neural network with the following structure:
Input (3 features)
→ Linear (64 units) + ReLU
→ Linear (128 units) + ReLU
→ Linear (16 outputs)
The output corresponds to the flattened lower-triangular matrix L.
---

## Training Objective
The model is trained using mean squared error loss between the predicted and target
Cholesky factors. Physical validity is enforced during reconstruction rather than through
explicit loss constraints.
---

## Evaluation Metrics
Performance is evaluated using:
- Quantum Fidelity
- Trace Distance
These metrics quantify the similarity and distinguishability between the predicted and
true density matrices on unseen test data.
---

## Results
The trained model achieves high reconstruction accuracy with mean fidelity above 0.9 and
low trace distance, demonstrating effective and physically consistent quantum state
reconstruction.
---

## References
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press.
- J. Watrous, *The Theory of Quantum Information*, Cambridge University Press.
- https://arxiv.org/abs/quant-ph/0005055
- https://arxiv.org/abs/1011.1939
