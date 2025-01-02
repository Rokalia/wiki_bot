from sentence_transformers import SentenceTransformer, CrossEncoder, util
from transformers import pipeline
import torch

def get_models():
  retriver = SentenceTransformer(
      model_name_or_path="DiTy/bi-encoder-russian-msmarco",
      cache_folder="./hf_cache",
      model_kwargs={"torch_dtype": "float16"}
  )
  
  reranker = CrossEncoder(
      model_name="DiTy/cross-encoder-russian-msmarco",
      cache_dir="./hf_cache",
      max_length=512
  )
  
  qa = pipeline(
     task='question-answering',
     model='timpal0l/mdeberta-v3-base-squad2'
     torch_dtype=torch.float16,
     use_safetensors=True,
  )
  return retriver, reranker, qa
