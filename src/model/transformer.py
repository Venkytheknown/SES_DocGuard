# File: /SES-DocGuard/SES-DocGuard/src/model/transformer.py

import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

class TransformerModel(nn.Module):
    def __init__(self, num_classes, hidden_size=768, num_attention_heads=12, num_encoder_layers=12, num_decoder_layers=12):
        super(TransformerModel, self).__init__()
        self.encoder = BertModel.from_pretrained('bert-base-uncased')
        self.fc = nn.Linear(hidden_size, num_classes)
        self.dropout = nn.Dropout(0.1)

    def forward(self, input_ids, attention_mask):
        encoder_outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = encoder_outputs[1]  # Get the pooled output
        output = self.dropout(pooled_output)
        return self.fc(output)

def initialize_model(num_classes):
    model = TransformerModel(num_classes=num_classes)
    return model

def load_pretrained_model(model_path):
    model = TransformerModel(num_classes=2)  # Adjust num_classes as needed
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def save_model(model, model_path):
    torch.save(model.state_dict(), model_path)