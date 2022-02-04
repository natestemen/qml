#This file was created to help desiging hybrid quantum-classical classifier based on VQAs.
#First lets see what are the expected 1.input  2.design and 3.output of the code

#1. Input: trainging set (features,class)=(X,y).  number of iterations, initial parameters 

#2. Design: There are various design elements 
#2.1 Quantum Circuit consisiting of Data embedding cirscuit and Ansatz
# Data embedding circuit: one of the design elements or "hyperparameters". freedom in choosing different built-in circuits (such as phase embedding, amplitude embedding, ZFeatureMap, ZZFeatureMap, ...) or designing one of your own. Data embedding circuit can include parameters to be optimized or it can only have input features (X) as the parameters.
# Ansatz Circuit: It is a parametrized circuit whose role is to find optimal measurement basis in the n-qubit Hilbert space 
# The "Quantum Circuit for VQA (QC-VQA)" will be Data Embedding Circuit followed by the Ansatz 
#2.2 Classical optimizer: can be chosen among SPSA, COBYLA, Gradient Descent, ...
#3. Output: Optimal parameters

# Steps of the CODE

# Prepare Input

# Design QC-VQA: Data Embedding cirscuit + Ansatz circuit

# Choose a measurement for QC-VQA parity or one-qubit

# Choose a classical optimizer

# Use built-in QNN functions either circuitQNN or Opflow
# The designed QC-VQA will be used in the so-called Quantum Neural Network (QNN) both in Forward pass and Backward pass\
# The forward pass gets the training set as input and finds the loss, the backward pass outputs updated parameters (based on the chosen classical optimizer) to be used in the next optimization step. 
# Inputs of circuitQNN: 
# Outputs of CircuitQNN:



