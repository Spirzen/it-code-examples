model.eval()
val_loss = 0.0
correct = 0
total = 0
with torch.no_grad():
    for batch_x, batch_y in val_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        logits = model(batch_x)
        val_loss += criterion(logits, batch_y).item()
        pred = logits.argmax(dim=1)
        correct += (pred == batch_y).sum().item()
        total += batch_y.size(0)

val_acc = correct / max(total, 1)
print(f"val_loss={val_loss:.4f}, val_acc={val_acc:.4f}")
