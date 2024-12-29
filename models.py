from sentence_transformers import SentenceTransformer, CrossEncoder, util
from transformers import pipeline

def get_models():
  retriver = SentenceTransformer(
      model_name_or_path="DiTy/bi-encoder-russian-msmarco",
      cache_folder="./hf_cache",
  )
  
  reranker = CrossEncoder(
      model_name="DiTy/cross-encoder-russian-msmarco",
      max_length=512
  )
  
  qa = pipeline(
     task='question-answering',
     model='timpal0l/mdeberta-v3-base-squad2'
  )
  return retriver, reranker, qa
