# -*- coding: utf-8 -*-
"""train_test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i2PekR0EP7wSd1XFbCCv-K_3N-PkE4tH

# Import Libraries
"""

# import all the required torch functions
from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
from tqdm import tqdm

from definitions import NormType, RegularizerType

"""# Training and Testing

- Looking at logs can be boring, so we'll introduce **tqdm** progressbar to get cooler logs. 
- Let's write train and test functions
"""

class TorchTrainTest:

  def __init__(self):
    self.train_losses = []
    self.test_losses = []
    self.train_acc = []
    self.test_acc = []

  # Private method
  def __reset(self):
    self.train_losses = []
    self.test_losses = []
    self.train_acc = []
    self.test_acc = []

  # Private method
  def __train(self,
        model, device, train_loader, loss_fn, optimizer, 
        regularizer_lambda=0.01, regularizer_type=RegularizerType.NONE):  
    
    model.train() # set the model with training mode (this is the default mode)

    pbar = tqdm(train_loader)
    correct = 0
    processed = 0
    for batch_idx, (data, target) in enumerate(pbar):
      # get samples
      data, target = data.to(device), target.to(device)

      # Init. 
      optimizer.zero_grad()
      # In PyTorch, we need to set the gradients to zero before starting to do backpropragation because PyTorch accumulates the gradients on subsequent backward passes. 
      # Because of this, when you start your training loop, ideally you should zero out the gradients so that you do the parameter update correctly.

      # Predict. 
      y_pred = model(data)

      # Calculate model prediction loss
      loss = loss_fn(y_pred, target)

      # Handle for L1 loss
      if RegularizerType.L1 == regularizer_type:
        l1 = 0
        for p in model.parameters():
          # absolute sum of all weights
          l1 += p.abs().sum()
        
        # Total loss is sum of model prediction loss + L1 loss
        loss += (regularizer_lambda * l1)

      self.train_losses.append(loss)

      # Backpropagation
      loss.backward()
      optimizer.step()

      # Update pbar-tqdm     
      pred = y_pred.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
      correct += pred.eq(target.view_as(pred)).sum().item()
      processed += len(data)

      pbar.set_description(desc= f'Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}')
      self.train_acc.append(100*correct/processed)

    return 100*correct/processed

  # Private method
  def __test(self, model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
      for data, target in test_loader:
        data, target = data.to(device), target.to(device)
        output = model(data)
        test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
        pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
        correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    self.test_losses.append(test_loss)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
    
    self.test_acc.append(100. * correct / len(test_loader.dataset))

    return 100. * correct / len(test_loader.dataset)

  # Public Method
  def train_test_model(self,
                model, device, train_loader, test_loader, epochs=20, 
                regularizer_lambda=0.01, regularizer_type=RegularizerType.NONE,
                sgd_lr=0.05, sgd_momentum=0.9, lr_step_size=6, lr_gamma=0.5):

    # reset all params before new train/test
    self.__reset()
    
    # create an optimizer (SGD) with required parameters, 
    # model.parameters() - these are the model parameters to optimize, 
    # learning-rate lr=0.01 and momentum-0.9
    optimizer = optim.SGD(model.parameters(), lr=sgd_lr, momentum=sgd_momentum)
    scheduler = StepLR(optimizer, step_size=lr_step_size, gamma=lr_gamma)

    prev_train_acc = -1
    prev_test_acc = -1
    train_accuracy = 0
    test_accuracy = 0

    # run single epoch as of now.
    for epoch in range(epochs):
        print(f'Epoch: {epoch+1}')

        # train the model loaded on the device with the required optimizer
        train_accuracy = __train(
                            model, device, train_loader, 
                            optimizer,
                            regularizer_lambda, 
                            regularizer_type)

        # set to the next lr params
        scheduler.step()

        # we need to evaluate on test data
        test_accuracy = __test(model, device, test_loader)

        # check difference from previous accuracies for better understanding
        if -1 == prev_train_acc:
          prev_train_acc = train_accuracy
        if -1 == prev_test_acc:
          prev_test_acc = test_accuracy

        print(f'train_acc_diff: {train_accuracy - prev_train_acc:.3f} test_acc_diff: {test_accuracy - prev_test_acc:.3f} test_train_diff: {test_accuracy - train_accuracy:.3f}\n')
        prev_train_acc = train_accuracy
        prev_test_acc = test_accuracy

    # update model metric
    model_metric = [train_losses, test_losses, train_acc, test_acc]
    return model_metric

from model import Net

# Check all model Summaries
norm_options = [NormType.BATCH_NORM, NormType.LAYER_NORM, NormType.GROUP_NORM]
norm_name = ["BATCH_NORM", "LAYER_NORM", "GROUP_NORM"]

# evaluation metrics for different models
evaluation_metrics = {}
model_metric = []

print(f"\nTrain & Evaluate different model\n")

oTrainTest = TorchTrainTest()

for ndx, norm in enumerate(norm_options):
  
  print(f"\nTrain & Test Model with NormalizationType => { norm }\n")
  
  # Create model instance with required params
  model = Net(norm_type=norm).to(device)

  # Map regularizer type as per the problem statement.
  regularizer = RegularizerType.NONE
  if NormType.BATCH_NORM == norm:
    regularizer = RegularizerType.L1

  # train the test model
  model_metric = oTrainTest.train_test_model(
                        model, device,
                        train_loader, test_loader, epochs=20, 
                        regularizer_lambda=0.01, regularizer_type=regularizer,
                        sgd_lr=0.05, sgd_momentum=0.9, lr_step_size=6, lr_gamma=0.5)

  # update final evaluation metrics for this model
  evaluation_metrics[norm_name[ndx]] = model_metric

"""# Plot the model's learning progress

- Plot training and test accuracies of all models
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [15, 6]

for name in norm_name:
  
  train_losses  = evaluation_metrics[name][0]
  test_losses   = evaluation_metrics[name][1]
  train_acc     = evaluation_metrics[name][2]
  test_acc      = evaluation_metrics[name][3]

  plt.subplot(2,2, 1)

  plt.plot(test_acc)
  plt.legend(norm_name)
  plt.title("Test Accuracy")

  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')

  plt.subplot(1,2,2)
  plt.plot(test_losses)
  plt.legend(norm_name)
  plt.title('Test Loss')
  plt.xlabel('Epoch')
  plt.ylabel('Loss')

"""# Move tesnors to numpy as required

- train_losses is a list, but train_losses[i] is a tensor
- all others are numpy

## APIs to use

- To go from np.array to cpu Tensor    => torch.from_numpy().
- To go from cpu Tensor to gpu Tensor  => .cuda()
- To go from a Tensor that requires_grad to one that does not => .detach() 
- To go from a gpu Tensor to cpu Tensor => .cpu()
- To gp from a cpu Tensor to np.array   => .numpy()
"""
