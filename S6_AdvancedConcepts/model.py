# -*- coding: utf-8 -*-

# import all the required torch functions
import torch
import torch.nn as nn
import torch.nn.functional as F
from definitions import *

class Net(nn.Module):

    def __init__(self, input_shape = (1, 28, 28), norm_type=NormType.BATCH_NORM, dropout_value=0.05):
        super(Net, self).__init__()

        # store the norm type for this instance. Control the code based on it
        self.norm_type = norm_type 
        self.dropout_value = dropout_value
        self.input_shape = input_shape
        self.changed_output_size = int(input_shape[1])
        self.norm_type = norm_type

        # Input Block
        self.changed_output_size -= 2 #based on conv2d params
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=8, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),            
            self.normalization_layer(self.norm_type, (8, self.changed_output_size, self.changed_output_size, 2)),
            nn.Dropout(self.dropout_value)
        ) # output_size = 26

        # CONVOLUTION BLOCK 1
        self.changed_output_size -= 2
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=15, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),
            self.normalization_layer(self.norm_type, (15, self.changed_output_size, self.changed_output_size, 3)),
            nn.Dropout(self.dropout_value)
        ) # output_size = 24

        # TRANSITION BLOCK 1
        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=15, out_channels=15, kernel_size=(1, 1), padding=0, bias=False),
        ) # output_size = 24

        self.pool1 = nn.MaxPool2d(2, 2) # output_size = 12
        self.changed_output_size /= 2

        # CONVOLUTION BLOCK 2
        self.changed_output_size -= 2
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=15, out_channels=15, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),            
            self.normalization_layer(self.norm_type, (15, self.changed_output_size, self.changed_output_size, 3)),
            nn.Dropout(self.dropout_value)
        ) # output_size = 10

        self.changed_output_size -= 2
        self.convblock5 = nn.Sequential(
            nn.Conv2d(in_channels=15, out_channels=15, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),            
            self.normalization_layer(self.norm_type, (15, self.changed_output_size, self.changed_output_size, 3)),
            nn.Dropout(self.dropout_value)
        ) # output_size = 8

        self.changed_output_size -= 2
        self.convblock6 = nn.Sequential(
            nn.Conv2d(in_channels=15, out_channels=15, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),            
            self.normalization_layer(self.norm_type, (15, self.changed_output_size, self.changed_output_size, 3)),
            nn.Dropout(self.dropout_value)
        ) # output_size = 6
        
        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=6)
        ) # output_size = 1
              
        self.convblock7 = nn.Sequential(
            nn.Conv2d(in_channels=15, out_channels=10, kernel_size=(1, 1), padding=0, bias=False),
        ) 

        self.dropout = nn.Dropout(self.dropout_value)

    def forward(self, x):
        x = self.convblock1(x)
        x = self.convblock2(x)
        x = self.convblock3(x)
        x = self.pool1(x)
        x = self.convblock4(x)
        x = self.convblock5(x)
        x = self.convblock6(x)
        x = self.gap(x)          
        x = self.convblock7(x)            

        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)

    def normalization_layer(self, norm_type, dimensions):
      # dimensions => C, H, W, N  (channel, height, width, Group_size for layer norm)

      if NormType.BATCH_NORM == norm_type:
        return nn.BatchNorm2d( dimensions[0] )
      elif NormType.LAYER_NORM == norm_type:
        dimension = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]
        return nn.LayerNorm( dimension, elementwise_affine=False ) # requires C, H, W
      elif NormType.GROUP_NORM == norm_type:
        # consider the group size in last parameter. 
        # note: Channels % group_size should be == 0
        return nn.GroupNorm( dimensions[3], dimensions[0] ) # requires group_number, channels(C)
      else:
        # default Batch Norm
        return nn.BatchNorm2d( dimensions[0] )

