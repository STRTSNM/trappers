import time
import multiprocessing
import torch
from transformers import BertTokenizerFast, BertForSequenceClassification, pipeline
from huggingface_hub import snapshot_download

def get_local_model_path(model_id: str) -> str:
    """
    Resolve the local snapshot path for a Hugging Face model ID.
    If it's already cached, it won't re-download.
    """
    return snapshot_download(model_id, local_files_only=True)

model_path1 = get_local_model_path("ealvaradob/bert-finetuned-phishing")

pipe1 = pipeline(
    "text-classification",
    model=model_path1
)

def inferText(p):
    print(f"Process {multiprocessing.current_process().name} is analyzing a chunk...")
    t1 = time.time()
    res = pipe1(p)
    t2 = time.time()
    print(f"Chunk processed in {t2 - t1:.4f}s with result: {res}")
    return res[0]


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Device set to use: {device}")


model_path2 = get_local_model_path("CrabInHoney/urlbert-tiny-v3-phishing-classifier")

tokenizer = BertTokenizerFast.from_pretrained(model_path2, local_files_only=True)
model = BertForSequenceClassification.from_pretrained(model_path2, local_files_only=True)
model.to(device)

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1,
    return_all_scores=True
)

def inferURL(url):
    label_mapping = {"LABEL_0": "good", "LABEL_1": "phish"}

    results = classifier(url)[0]
    print(results[1])
    return results[1]['score']


#inferURL("https://google.com")

