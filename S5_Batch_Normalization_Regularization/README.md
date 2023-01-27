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


