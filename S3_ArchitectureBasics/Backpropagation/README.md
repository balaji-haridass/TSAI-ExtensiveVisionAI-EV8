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
        
## Network Diagram (FC) 

![Network Diagram](https://user-images.githubusercontent.com/87327563/212443277-f709d8b3-c98f-42e0-9f4c-53e8cb238319.png)

- It is fully connected network
- t1, t2 are the target values against which we need to compare the loss to do the back-propagation
- Initial values with weights are provided. No bias is included as part of this network
- The activation function used in the hidden layers is Sigmoid (σ) 

        
```math
 σ(z) = \frac{1}{1+\mathrm{e}^{-z}}
```

# *Solution*

## Forward Propagation

### Let us discuss about inputs and outputs of Individual Neurons

In a fully-connected network, every neuron in each layer gets input from all the neurons from the previous layer.

**h1**
- h1 takes input from i1 & i2 with their corresponding weights w1 & w2. So

        h1 = w1 * i1 + w2 * i2

- The output of h1 has to be passed to the next layer. 

**a_h1**
- Since h1 is a linear equation, passing the same across the networks, collapses all layers to act like a single layer linear network. This looses capability to recognize complex patterns
- So we need to add non-linearity before passing h1 to the next layer as input.
- Activation function is used to add non-linearity. In our model, we will use Sigmoiud as activation function
- σ is a non-linear function. This adds non-linearity to h1, which can then be passed to the next layer

        a_h1 = σ(h1)

**h2, a_h2**
- similar to h1, 

        h2 = w3 * i1 + w4 * i2 => a_h2 = σ(h2)
        o1 = w5 * a_h1 + w6 * a_h2 => a_o1 = σ(o1)
        o2 = w7 * a_h1 + w8 * a_h2 => a_o2 = σ(o2)

Now that we got the values of a_o1 & a_o2

## Backward Propagation

- The goal of Backward propagation is to update the network's trainable parameters in such a way that the overall loss of the network is reduced.
- This means what the network predicts should match or closely match with the target values t1 & t2.
- So a_o1 & a_o2 should closely match with t1 & t2 respectively

### Identifing loss

- How to check if a_o1 & a_o2  matches with target values t1 & t2 respectively
- This requires a loss function. Loss calculates how much the predicted and the target values are different
- Less the loss, the closer or better match they are
- In this model, we are using L2 loss, which is the mean of squared differences

        E1 = ½ * (t1 - a_o1)^2
        E2 = ½ * (t1 - a_o1)^2
        E_Total = E1 + E2
        
### Acting to reduce loss

- Now that we identified the loss. Next step is to change the network in such a way that the loss reduces in the next interation
- To change the network, we can update the weight which define the network. In this network there are bias, so we will only update weights

### How to update weights?

- Weights are the one that contributes to the foward propagation
- Some weight that contirbute more to the error, some less
- So we need to find the rate of change of E_Total w.r.t to Individual Weights. That is identify how a small change in Wi will affect E_Total

        Calculate ∂E_Total/∂Wi  ; Where i represent each of the weights in the network

- Once we identify the rate of change then we can weights accordingly
  - If it is more, then it means we need to go a long way to reach the minima, so we can step more/long
  - If it is less, then we can close by, so update little, so that we don't miss the minima
        
        For each of the weights, do
                Wi = Wi - ⴄ * ∂E_Total/∂Wi
                
                ⴄ is the learning rate. Helps to define how much more i can trim downor(or pull up) the updates, could be 1, 0.1, 0.01, 0.001 etc


### How to calculate ∂E_Total/∂Wi

- Lets consider w5

        ∂E_Total/∂w5 = ∂(E1 + E2)/∂w5
        
        Here, w5 has no impact on E2, so the derivative is constant, leading to
        
        ∂E_Total/∂w5 = ∂E1/∂w5

- w5 does not directly impact E1, but through many intermediates
- The rate at which w5 changes E1 (∂E1/∂W5), is dependent on how
  - w5 changes o1, in turn how o1 changes a_o1 and how a_o1 changes E1
  - So we can caculate this easily with partial derivates
  
        ∂E_Total/∂w5 = ∂E1/∂w5 = (∂E1/∂a_o1) * (∂a_o1/∂o1) * (∂o1/∂w5)
        
- Now we can easily calculate each of these derivatives and then substitute them and calculate ∂E_Total/∂w5
- In the same way we can calculate all ∂E_Total/∂Wi

### Formulas derived to calculate all weights
 
![Back-Propagation-Formulas](https://user-images.githubusercontent.com/87327563/212445866-2aca2daf-4a06-4bd2-8ee3-7901ea723f2d.png)


# Verifying the above formulas in XL

- Please check the file S3_NN_BackPropagation.xlsx, present in this folder for all the formulas included
- All the above formula are key-ed in, so that we can check with different values
  - Data for w1 to w8, t1, t2, i1, i2 can we changed and checked for loss
- The xls includes back-propagation updates for ~70 steps. With this we trained a simple network in the xls sheet

Let us change the learning rate in the XLS, to different values and check how the loss changes across these 70 steps


| Learning Rate (ⴄ) | Loss Plot from Xls | Description |
| :---:  | :---:  | --- |
| 0.1 | <img src="https://user-images.githubusercontent.com/87327563/212446263-c2a0d39a-fcae-420d-8526-4b18b6ef03ea.png" width="400" height="400"> | Learning is slower.  |
| 0.2 | <img src="https://user-images.githubusercontent.com/87327563/212446368-844cda0b-c2e8-4395-a05c-7358e5f1cf65.png" width="400" height="400"> | Starts to coverge faster |
| 0.5 | <img src="https://user-images.githubusercontent.com/87327563/212446408-e8e727d1-4208-4114-99f9-a08f949af55f.png" width="400" height="400"> | Coverges faster than 0.2 |
| 0.8 | <img src="https://user-images.githubusercontent.com/87327563/212446437-7e21c807-19f7-4709-a1c8-f511a79fb15e.png" width="400" height="400"> | Coverges faster than 0.5 |
| 1.0 | <img src="https://user-images.githubusercontent.com/87327563/212446448-be879917-d11c-484a-b401-fc5db827717a.png" width="400" height="400"> | Coverges faster than 1.0 |
| 2.0 | <img src="https://user-images.githubusercontent.com/87327563/212446513-242899af-b29d-492a-af79-9424324e6528.png" width="400" height="400"> | Coverges faster than 1.0 |


This clearly explain how learning rate impacts convergence. 
- We can change the values for w1 to w8, t1, t2, i1, i2  and checke for convergence
- Please feel free to download and experiment with the xls sheet

