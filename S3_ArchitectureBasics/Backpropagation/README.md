# **BackPropagation**
## **Part 1 of Assignment**

### Problem Statement

**Rewrite the whole excel sheet showing backpropagation.**

        1. Explain each major step, and write it on Github. 
        2. Use exactly the same values for all variables as used in the class
        3. Take a screenshot, and show that screenshot in the readme file
        4. The Excel file must be there for us to cross-check the image shown on readme (no image = no score)
        6. Explain each major step
        7. Show what happens to the error graph when you change the learning rate from [0.1, 0.2, 0.5, 0.8, 1.0, 2.0] 
        
# Network Diagram (FC) 

![Network Diagram](https://user-images.githubusercontent.com/87327563/212443277-f709d8b3-c98f-42e0-9f4c-53e8cb238319.png)

- It is fully connected network
- t1, t2 are the target values against which we need to compare the loss to do the back-propagation
- Initial values with weights are provided. No bias is included as part of this network
- The activation function used in the hidden layers is Sigmoid (σ) 

        
```math
 σ(z) = \frac{1}{1+\mathrm{e}^{-z}}
```
