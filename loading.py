import torch
torch.manual_seed(1337)

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# here are all the unique characters that occur in this text
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l])
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = GPTLanguageModel().to(device)
model.load_state_dict(torch.load('hatemodel.pth'))
model.eval()
context = torch.zeros((1,1),dtype = torch.long,device = device)
print(decode(model.generate(context, max_new_tokens = 200)[0].tolist()))