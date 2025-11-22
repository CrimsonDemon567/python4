# ai_helper_torch.py
# Utility module to support AI development with PyTorch

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, f1_score

class AITrainer:
    def __init__(self, model, lr=0.001, device=None):
        self.model = model
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.criterion = nn.CrossEntropyLoss()

    def train_epoch(self, dataloader):
        """Train the model for one epoch."""
        self.model.train()
        total_loss = 0
        for X, y in dataloader:
            X, y = X.to(self.device), y.to(self.device)
            self.optimizer.zero_grad()
            outputs = self.model(X)
            loss = self.criterion(outputs, y)
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
        return total_loss / len(dataloader)

    def evaluate(self, dataloader):
        """Evaluate the model and return accuracy + F1."""
        self.model.eval()
        all_preds, all_labels = [], []
        with torch.no_grad():
            for X, y in dataloader:
                X, y = X.to(self.device), y.to(self.device)
                outputs = self.model(X)
                preds = torch.argmax(outputs, dim=1)
                all_preds.extend(preds.cpu().numpy())
                all_labels.extend(y.cpu().numpy())
        return {
            "accuracy": accuracy_score(all_labels, all_preds),
            "f1": f1_score(all_labels, all_preds, average="weighted")
        }

    def save(self, path="model.pt"):
        """Save model weights."""
        torch.save(self.model.state_dict(), path)
        print(f"[AITrainer] Model saved to {path}")

    def load(self, path="model.pt"):
        """Load model weights."""
        self.model.load_state_dict(torch.load(path, map_location=self.device))
        self.model.to(self.device)
        print(f"[AITrainer] Model loaded from {path}")
