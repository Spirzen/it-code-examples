class TinyTransformerClassifier(nn.Module):
    def __init__(self, vocab_size, d_model=128, num_heads=4,
                 d_ff=512, num_layers=2, num_classes=2, max_len=128):
        super().__init__()
        self.token_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Embedding(max_len, d_model)
        self.layers = nn.ModuleList([
            EncoderBlock(d_model, num_heads, d_ff) for _ in range(num_layers)
        ])
        self.head = nn.Linear(d_model, num_classes)

    def forward(self, input_ids):
        batch, seq_len = input_ids.size()
        positions = torch.arange(seq_len, device=input_ids.device).unsqueeze(0)
        x = self.token_emb(input_ids) + self.pos_emb(positions)
        for layer in self.layers:
            x = layer(x)
        # [CLS]-подобный pooling — первый токен
        return self.head(x[:, 0, :])
