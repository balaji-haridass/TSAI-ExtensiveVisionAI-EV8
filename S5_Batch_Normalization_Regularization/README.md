# Normalization (Batch, Layer, Group, Instance) & Regularization (L1, L2)

## Problem Statement

Make 3 versions of your 4th assignment's best model (or pick one from best assignments):
  1. Network with Group Normalization
  2. Network with Layer Normalization
  3. Network with L1 + BN

## Guidelines

- Write a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include
- Write a single notebook file to run all the 3 models above for 20 epochs each
- Create these graphs:
  Graph 1: Test/Validation Loss for all 3 models together
  Graph 2: Test/Validation Accuracy for 3 models together
  graphs must have proper annotation

- Find 10 misclassified images for each of the 3 models, and show them as a 5x2 image matrix in 3 separately annotated images. 
- write an explanatory README file that explains:
  - what is your code all about,
  - how to perform the 3 normalizations techniques that we covered(cannot use values from the excel sheet shared)
  - your findings for normalization techniques,
  - add all your graphs
  - your 3 collection-of-misclassified-images 

# Reference

- *Important* => [Comparison of Batch, Layer, Instance and Group Normalization](https://www.youtube.com/watch?v=CuEU-VH6Fdw) by Hüseyin Özdemir

| Topic | Links |
| :---:  | :---:  |
| Batch Normalization | [BN by Hüseyin Özdemir](https://www.youtube.com/watch?v=a-2dH0Bu2Us) |
| Layer Normalization | [LN by Hüseyin Özdemir](https://www.youtube.com/watch?v=6-EOXaP9q-o) |
| Instance Normalization | [IN by Hüseyin Özdemir](https://www.youtube.com/watch?v=YG60dtlLfGo) |


# What is your code all about

The code is built to test the performance of the models w.r.t to different Normalization layers (Batch, Layer, Group Normalization layers)

## Code Structure
- The code is split modulary, to seperate the model from the training/test apis 
- Definitions.py: Has all the definitions for normalization and regularizaiton types
- Net class (in model.py) 
  - Defines the torch model with the architecture specified
  - It has API to return the required Normalization layer based on parameters passed to it
  - Includes the definitions.py
- The main file: EV8_S5_NormalizationTypes_Split.ipynb
  - Includes the definition.py and model.py
  - Creates model instance with the required parametrs of regularization, normalization values
  - Compares the peformance of the different normalization types
 
# How Noramalization is performed

- Normalization helps to standardize all output values before it is fed as input to the next layer
- This help all layers to see input of similar range and this also helps the weights be within the range.
- Different Normalization exhbits different behaviors. We need to evaluate them.
- Let us discuss the different normalizations with CNN

## Input, kernel/Filter, Channel Output representation

![Component_Rep](https://user-images.githubusercontent.com/87327563/216779433-dc76d230-475b-4ecd-bc75-d9ca23f74d60.png)

## Batch Normalization

![Batch_Norm](https://user-images.githubusercontent.com/87327563/216779473-ee875102-4ab4-4be4-b898-8eb1c3d8bc34.png)

## Layer Normalization

![Layer_Norm](https://user-images.githubusercontent.com/87327563/216779516-6599ec99-9f5c-4f50-947b-b52b9402ffc4.png)

## Group Normalization

![Group_Norm](https://user-images.githubusercontent.com/87327563/216779605-aea1de6c-f388-47c2-b689-74f739bdef31.png)

# Accuracy and Loss Plots

![Accuracy & Loss Plots](https://user-images.githubusercontent.com/87327563/216777257-fbc30d6f-ba16-481c-b8fb-352621827bc4.png)

Following are the observation from graphs
- Group loss is lower when compared the other too
- Eventually all converge close to similar accuracy (by 20 Epochs), with group norm perfoming relatively higher
- Batch Norm model's test accuracy varies a lot
  
# Misclassified Files

## Batch Norm + L1

![BN_Plots](https://user-images.githubusercontent.com/87327563/216777047-b2902e6f-1bee-4462-a559-03f823aee4c4.png)

## Layer Norm

![LN_Plits](https://user-images.githubusercontent.com/87327563/216777158-493a7053-92f3-4ff2-9cfe-673beb14c5bf.png)

## Group Norm

![GN_Plots](https://user-images.githubusercontent.com/87327563/216777225-c1cf7944-b402-4126-b64c-11f8db60ae41.png)
