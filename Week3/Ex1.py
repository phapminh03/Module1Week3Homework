import torch
import torch.nn as nn

class SoftMax(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        return torch.exp(x-max(x))/sum(torch.exp(x-max(x)))

data = torch.Tensor([1,2,3])
res = SoftMax()
print(res(data))