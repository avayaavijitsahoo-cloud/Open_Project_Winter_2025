# Assignment 3 Report: Scalable Quantum Tomography Pipelines

## Method
We implemented a scalable surrogate model for quantum state tomography that supports an
arbitrary number of qubits. The model dynamically adapts its output dimension to 2^n and
supports serialization using pickle for reproducibility.

## Scalability Results
Experiments were conducted for 2–5 qubits. As the number of qubits increases, fidelity
generally decreases while computational cost increases due to exponential state growth.

## Ablation Study
An ablation study on model capacity (hidden dimension) shows that increased capacity can
improve expressiveness, though results are affected by random initialization.

## Limitations
The model is not explicitly trained and uses proxy fidelity metrics.

## Future Work
Future work includes classical shadows, parameter-efficient models, and hardware validation.