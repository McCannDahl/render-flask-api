from haystack.document_stores import PineconeDocumentStore
from haystack.nodes import PreProcessor, EmbeddingRetriever
from haystack.nodes import FARMReader
from haystack.nodes import Seq2SeqGenerator
import os

APIKEY = os.environ['APIKEY']

pineconeIndex = 'lds-test'
pineconeEnv = "asia-southeast1-gcp-free"

document_store = PineconeDocumentStore(
    APIKEY,
    environment=pineconeEnv,
    similarity="cosine",
    index=pineconeIndex,
    embedding_dim=384,
)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="multi-qa-MiniLM-L6-cos-v1",
    model_format="sentence_transformers"
)

# preprocessor = PreProcessor(
#     clean_whitespace=True,
#     clean_header_footer=True,
#     clean_empty_lines=True,
#     split_by="word",
#     split_length=200,
#     split_overlap=20,
#     split_respect_sentence_boundary=True,
# )

# reader = FARMReader(
#     model_name_or_path='deepset/electra-base-squad2', 
#     use_gpu=True
# )

# generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")