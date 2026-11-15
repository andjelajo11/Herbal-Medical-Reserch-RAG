from datasets import load_dataset
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.query import Filter
from typing import List
from tqdm import tqdm
import joblib
import weaviate
import re
from weaviate.util import generate_uuid5
from pprint import pprint
import os

# BeIR/nfcorpus has 3 splits
corpus = load_dataset("BeIR/nfcorpus", "corpus", split="corpus")   # 3,633 docs: _id, title, text
queries = load_dataset("BeIR/nfcorpus", "queries", split="queries") # 323 queries

corpus.list(:5)