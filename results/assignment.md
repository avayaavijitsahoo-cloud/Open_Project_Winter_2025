### Task 1 : Serialization basics
To store trained surrogate models and intermediate results, I use Python’s pickle serialization. Pickle can serialize arbitrary Python objects, including NumPy arrays, class instances, and dictionaries, which makes it suitable for rapid prototyping and checkpointing during experiments

## Advantages of pickle:
- Simple to use with minimal boilerplate
- Preserves full Python object structure
- Fast for small to medium models

## Limitations:
- Python-specific and not language-agnostic
- Not safe against untrusted inputs
- Less efficient for very large numerical datasets

## For large-scale experiments or long-term storage, a format such as HDF5 is preferable because it:
- Handles large numerical arrays efficiently
- Supports partial loading
- Is language-independent and widely supported

In this assignment, pickle is sufficient because the models are lightweight and only reused within the same Python environment.

### Task 2 : Extendable n-qubit surrogate
The surrogate model is designed to scale with the number of qubits n by parameterising the Hilbert space dimension as 2^n.The model supports optional noise and is seeded for reproducibility. This structure allows controlled scalability studies while keeping the implementation simple and interpretable.

### Task 3 : Scalability study
To study scalability, fidelity and runtime are evaluated as a function of the number of qubits. For each system size, multiple random seeds are used and the results are averaged. This isolates scaling trends from statistical fluctuations.

### Task 4 : Visualise scalability metrics
The scalability metrics are visualised by plotting mean fidelity and runtime versus the number of qubits. Runtime shows exponential growth due to the increasing Hilbert space dimension, while fidelity degrades mildly as noise and numerical effects accumulate.

### Task 5 : Ablation studies
Ablation studies isolate how architectural choices affect performance. Here, circuit depth is varied while holding all other parameters constant. Increased depth improves expressibility but also increases runtime and susceptibility to noise.

### Task 6 : Reporting and submission
This work investigated the scalability of a surrogate-based quantum tomography pipeline. As the number of qubits increases, both runtime and memory usage grow rapidly due to the exponential growth of the Hilbert space. While fidelity remains reasonable for small systems, scalability becomes a limiting factor beyond a few qubits. Ablation studies show that increased expressibility improves reconstruction quality but introduces additional computational cost. Future work could integrate compressed sensing or classical shadow techniques to mitigate exponential scaling and enable practical tomography on larger quantum systems.
