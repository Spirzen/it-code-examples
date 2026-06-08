from llama_cpp import Llama

llm = Llama(
    model_path="models/llama-3-8b.Q5_K_M.gguf",
    n_ctx=8192,
    n_gpu_layers=35,
    verbose=False
)

output = llm(
    "Объясни, как работает HTTP-запрос.",
    max_tokens=512,
    temperature=0.3,
    top_p=0.9,
    repeat_penalty=1.1
)
print(output["choices"][0]["text"])
