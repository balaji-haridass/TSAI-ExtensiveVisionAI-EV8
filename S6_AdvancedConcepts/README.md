# Advanced Concepts

## Problem Statement - From S6

- Run this ![network](https://colab.research.google.com/drive/1qlewMtxcAJT6fIJdmMh8pSf2e-dh51Rw)
- Fix the network above:
  - Change the code such that it uses GPU and
  - Change the architecture to C1C2C3C40 
    - No MaxPooling, but 3 3x3 layers with stride of 2 instead
    - If you can figure out how to use Dilated kernels here instead of MP or strided convolution, then 200pts extra!
  - Total RF must be more than 44
  - One of the layers must use Depthwise Separable Convolution
  - One of the layers must use Dilated Convolution
  - Use GAP (compulsory):- add FC after GAP to target #of classes (optional)
  - Use albumentation library and apply:
    - Horizontal flip
    - ShiftScaleRotate
    - CoarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)
  - Achieve 85% accuracy, as many epochs as you want. Total Params to be less than 200k.

## Problem Statement - From S5

Change your code in such a way that all of these are in their respective files:
- model
- training code
- testing code
- regularization techniques (dropout, L1, L2, etc)
- dataloader/transformations/image-augmentations
- misc items like finding misclassified images
