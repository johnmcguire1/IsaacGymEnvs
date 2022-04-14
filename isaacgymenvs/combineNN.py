import torch

nn0 = torch.load('runs/Cartpole/nn0/Cartpole.pth')
nn1 = torch.load('runs/Cartpole/nn1/Cartpole.pth')
nn2 = torch.load('runs/Cartpole/nn0/last_Cartpoleep101rew[490.87].pth')

"""
print("value_mean_std.running_mean: ")
print(nn1['model']['value_mean_std.running_mean'].item())

print("value_mean_std.running_var: ")
print(nn1['model']['value_mean_std.running_var'].item())

print("value_mean_std.count: ")
print(nn1['model']['value_mean_std.count'].item())

print("running_mean_std.running_mean: ")
print(nn1['model']['running_mean_std.running_mean'])

print("running_mean_std.running_var: ")
print(nn1['model']['running_mean_std.running_var'])

print("running_mean_std.count: ")
print(nn1['model']['running_mean_std.count'].item())

print("a2c_network.sigma: ")
print(nn1['model']['a2c_network.sigma'].item())

print("a2c_network.actor_mlp.0.weight: ")
print(nn1['model']['a2c_network.actor_mlp.0.weight'])

print("a2c_network.actor_mlp.0.bias: ")
print(nn1['model']['a2c_network.actor_mlp.0.bias'])

print("a2c_network.actor_mlp.2.weight: ")
print(nn1['model']['a2c_network.actor_mlp.2.weight'])

print("a2c_network.actor_mlp.2.bias: ")
print(nn1['model']['a2c_network.actor_mlp.2.bias'])

print("a2c_network.value.weight: ")
print(nn1['model']['a2c_network.value.weight'])

print("a2c_network.value.bias: ")
print(nn1['model']['a2c_network.value.bias'])

print("a2c_network.mu.weight: ")
print(nn1['model']['a2c_network.mu.weight'])

print("a2c_network.mu.bias: ")
print(nn1['model']['a2c_network.mu.bias'])
"""
print(nn2['model'].keys())

for key in nn1['model'].keys():
    print((nn0['model'][key] + nn1['model'][key]) / 2)

def averageNNs(nn0_path, nn1_path):

    """
    nn0 = torch.load(nn0_path)
    nn1 = torch.load(nn1_path)
    
    value_running_mean_tensor = 
    value_running_var_tensor = 
    value_count_tensor = 

    running_running_mean_tensor = 
    running_running_var_tensor = 
    running_count_tensor = 

    a2c_sigma_tensor = 

    a2c_0_weight_tensor = 
    a2c_0_bias_tensor = 

    a2c_2_weight_tensor = 
    a2c_2_bias_tensor = 

    a2c_value_weight_tensor = 
    a2c_value_bias_tensor =

    a2c_mu_weight_tensor = 
    a2c_mu_bias_tensor = 
    """



#print(nn0.named_parameters())

#Average all parameters

#for key in nn0:
#    nn0[key] = (nn0[key] + nn1[key])/2
#    nn1[key] = nn0[key]

#print(nn0)

#torch.save(nn0, 'runs/Cartpole/nn0/Cartpole.pth')
#torch.save(nn1, 'runs/Cartpole/nn1/Cartpole.pth')


