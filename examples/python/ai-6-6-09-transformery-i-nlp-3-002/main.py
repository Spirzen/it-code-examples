class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        batch, seq_len, d_model = x.size()
        q = self.w_q(x).view(batch, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        k = self.w_k(x).view(batch, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        v = self.w_v(x).view(batch, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        out, _ = scaled_dot_product_attention(q, k, v, mask)
        out = out.transpose(1, 2).contiguous().view(batch, seq_len, d_model)
        return self.w_o(out)
