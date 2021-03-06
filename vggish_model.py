import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class VGGish(nn.Module):
	def __init__(self):
		super(VGGish, self).__init__()

		self.layer1_conv1 = nn.Sequential(nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1), nn.ReLU())
		self.layer2_pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

									
		self.layer3_conv2 = nn.Sequential(nn.Conv2d(64, 128,kernel_size=3, stride=1, padding=1), nn.ReLU())
		self.layer4_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

		self.layer5_conv3_1 = nn.Sequential(nn.Conv2d(128, 256,kernel_size=3, stride=1,padding=1), nn.ReLU())
		self.layer6_conv3_2 = nn.Sequential(nn.Conv2d(256, 256,kernel_size=3, stride=1,padding=1), nn.ReLU())
		self.layer7_pool3 = nn.MaxPool2d(kernel_size=2, stride=2)

		self.layer8_conv4_1 = nn.Sequential(nn.Conv2d(256, 512,kernel_size=3, stride=1,padding=1), nn.ReLU())
		self.layer9_conv4_2 = nn.Sequential(nn.Conv2d(512, 512,kernel_size=3, stride=1,padding=1), nn.ReLU())
		self.layer10_pool4 = nn.MaxPool2d(kernel_size=2, stride=2)

		self.layer11_fc1 = nn.Sequential(nn.Linear(12288, 4096), nn.ReLU())
		self.layer12_fc2 = nn.Sequential(nn.Linear(4096, 4096), nn.ReLU())
		self.layer13_fc3 = nn.Sequential(nn.Linear(4096, 128), nn.ReLU())

	
	def forward(self, x):
		
		x = x.view(x.size(0), 1, x.size(1), x.size(2))

		out = self.layer1_conv1(x)
		out = self.layer2_pool1(out)

		out = self.layer3_conv2(out)
		out = self.layer4_pool2(out)

		out = self.layer5_conv3_1(out)
		out = self.layer6_conv3_2(out)
		out = self.layer7_pool3(out)

		out = self.layer8_conv4_1(out)
		out = self.layer9_conv4_2(out)
		out = self.layer10_pool4(out)

		out = out.permute(0, 2, 3, 1)
		out = torch.reshape(out, shape = (-1,12288))
		
		out = self.layer11_fc1(out)
		out = self.layer12_fc2(out)
		out = self.layer13_fc3(out)

		return out