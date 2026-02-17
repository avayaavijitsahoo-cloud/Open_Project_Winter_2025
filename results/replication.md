# Replication Guide

## Environment Setup
Python version: 3.9+
Install dependencies:
pip install numpy torch scipy tqdm matplotlib qutip
---

## Project Structure
- data.py
- model.py
- train.py
- metrics.py
- model.pt
- model_working.md
- replication.md
---

## Dataset Generation
The dataset is generated synthetically using random valid density matrices constructed
via Cholesky decomposition.
---

## Training
To train the model, run:
python train.py
The trained model is saved to outputs/model.pt.
---

## Evaluation
Evaluation metrics (fidelity and trace distance) can be computed by running the
evaluation cells in exp.ipynb.
---

## Reproducibility
All randomness can be controlled by setting fixed NumPy and PyTorch seeds.
The project does not rely on external datasets or hardware acceleration.
