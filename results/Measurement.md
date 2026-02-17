# Quantum State Tomography – Measurement & State Preparation

## Environment Information
- **OS:** macOS Tahoe 26.2
- **Python:** 3.13
- **Architecture:** arm64

---

## Task 2: Measurement Theory Primer

### 1. Born Rule
In quantum mechanics, physical systems are described by a quantum state, represented
either as a **statevector** |ψ⟩ or a **density matrix** ρ. Quantum states cannot be
observed directly. Instead, measurements are performed to obtain classical outcomes.

The **Born rule** provides the fundamental link between a quantum state and measurement
outcomes.
If a system is in state ∣ψ⟩ and we measure an observable with eigenstates ∣i⟩, then the probability of obtaining outcome i is:  P(i)=∣⟨i∣ψ⟩∣2
For a general measurement operator 𝑀𝑖, the probability of outcome i is: P(i)=Tr(ρMi​).
The Born rule underpins all quantum measurement theory and quantum state tomography.

---

### 2. Pauli Projective Measurements and Completeness
Completeness check:
For a single qubit, the Pauli-Z measurement consists of two projectors:
P₀ = |0⟩⟨0|
P₁ = |1⟩⟨1|

These projectors satisfy the completeness relation:
P₀ + P₁ = |0⟩⟨0| + |1⟩⟨1| = I

Thus, Pauli-Z measurements form a complete projective measurement.

#### Numerical Completeness Check

```python
import numpy as np

P0 = np.array([[1, 0],
               [0, 0]])

P1 = np.array([[0, 0],
               [0, 1]])

S = P0 + P1
I = np.eye(2)

print("Sum of operators:\n", S)
print("Is close to identity?", np.allclose(S, I))

I adopt Pauli projective measurements as it is simple,matches classical shadows and easy to serialize.
### Measurement Model Choice: Pauli Projective Measurements

**Pros**
- Simple and well-understood measurement framework
- Easy to implement both numerically and experimentally
- Widely used in quantum state tomography and classical shadows
- Operators are orthogonal and satisfy completeness exactly

**Cons**
- Requires multiple measurement settings (X, Y, Z)
- Not optimal in terms of measurement efficiency compared to SIC POVMs
- Assumes idealized projective measurements

## State Preparation Circuits:

### |0⟩
Initial state of the qubit. No gates applied.

### |1⟩
Prepared by applying an X gate to |0⟩.

### |+⟩
Prepared by applying a Hadamard (H) gate to |0⟩.

### |−⟩
Prepared by applying an X gate followed by a Hadamard gate.

### (|0⟩ + i|1⟩)/√2
Prepared by applying a Hadamard gate followed by an S gate.

## Task 3: QST Data generation

For each reference state:
- Circuits were executed on the PennyLane simulator
- Pauli-axis measurements were performed
- Measurement shots were collected
- Raw counts and empirical probabilities were computed

Artifacts were stored as:
- .npy / .npz measurement files
- JSON metadata (state, shots, measurement model)
- Ground-truth density matrices

## Task 4: Single-Qubit Tomography

Single-qubit density matrices were reconstructed using linear inversion:​
        ⍴=1/2(I+⟨X⟩X+⟨Y⟩Y+⟨Z⟩Z)
Expectation values were estimated from finite-shot measurement outcomes.
Ground-truth density matrices were obtained directly from the simulator for validation

## Task 5:Validation and Reporting

For each state, fidelity and trace distance were computed and aggregated into tables.
Trend analysis showed that reconstruction fidelity improves monotonically with increasing shot count, consistent with reduced statistical noise.
Density-matrix histograms were generated for both reconstructed and true states to visually compare magnitude and structure of matrix elements.
Multi-qubit visualizations were not fully explored in this phase due to exponential scaling, but the framework is extensible to two-qubit systems.

Sources of Error:
- Shot Noise: Finite sampling leads to statistical fluctuations in expectation values.
- Model Mismatch: Linear inversion does not enforce physical constraints such as positivity.
- Simulator Effects: Finite precision and sampling approximations introduce small errors.

“I documented the measurement theory, validated operator completeness both analytically and numerically, justified the use of Pauli projective measurements, and clearly described the synthesis of all reference states.”