import torch                                                                                                                                                                                                                                
import torch_xla                                                                                                                                                                                                                            
import torch_xla.core.xla_model as xm                                                                                                                                                                                                       
import torch_xla.debug.metrics as met                                                                                                                                                                                                       
import torch.nn as nn                                                                                                                                                                                                                       
from torch.autograd import Variable                                                                                                                                                                                                         
                                                                                                                                                                                                                                            
device = xm.xla_device()                                                                                                                                                                                                                    
output = torch.FloatTensor([0, 0, 0, 1]).to(device).view(1, -1).requires_grad_()                                                                                                                                                            
target = torch.LongTensor([3]).to(device)                                                                                                                                                                                                   
                                                                                                                                                                                                                                            
criterion = nn.CrossEntropyLoss()                                                                                                                                                                                                           
loss = criterion(output, target)                                                                                                                                                                                                            
print(loss.item())                                                                                                                                                                                                                          
loss.backward()                                                                                                                                                                                                                             
print(met.metrics_report())
