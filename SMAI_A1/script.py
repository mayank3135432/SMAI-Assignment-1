import torch
data = torch.load("path_to_file.pth", map_location="cpu")
print(type(data), data.keys() if isinstance(data, dict) else data.shape)

