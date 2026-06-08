
import torch

from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("my-ticket-model")
model.eval()
dummy = torch.randint(0, 1000, (1, 128))
torch.onnx.export(
    model,
    (dummy,),
    "ticket_classifier.onnx",
    input_names=["input_ids"],
    output_names=["logits"],
    dynamic_axes={"input_ids": {0: "batch", 1: "seq"}, "logits": {0: "batch"}},
    opset_version=17,
)
