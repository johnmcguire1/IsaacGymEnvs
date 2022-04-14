import filecmp
import torch

f = torch.load('runs/Cartpole/nn1/Cartpole.pth')
torch.save(f, 'runs/Cartpole/nn1/Cartpole_copy.pth')

print(filecmp.cmp('runs/Cartpole/nn1/Cartpole.pth', 'runs/Cartpole/nn1/Cartpole_copy.pth'))
print(f.keys())
