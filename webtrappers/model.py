import time
import multiprocessing
from transformers import pipeline

pipe = pipeline("text-classification", model="ealvaradob/bert-finetuned-phishing")



def infer(p):
    print(f"Process {multiprocessing.current_process().name} is analyzing a chunk...")
    t1 = time.time()
    res = pipe(p)
    t2 = time.time()
    print(f"Chunk processed in {t2 - t1:.4f}s with result: {res}")
    return res[0]
