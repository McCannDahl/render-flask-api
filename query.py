
from haystack.pipelines import ExtractiveQAPipeline, DocumentSearchPipeline, GenerativeQAPipeline
from shared import reader, retriever, generator

querying_pipeline = ExtractiveQAPipeline(reader, retriever)
generative_pipeline = GenerativeQAPipeline(generator, retriever)
search_pipe = DocumentSearchPipeline(retriever)
params = {
    "Retriever": {"top_k": 5},
}

def queryDocuments(input):
    answer = search_pipe.run(
        query=input,
        params=params
    )
    return answer
def queryExtractive(input):
    answer = querying_pipeline.run(
        query=input,
        params=params
    )
    return answer
def queryGenerative(input):
    answer = generative_pipeline.run(
        query=input,
        params=params
    )
    return answer

if __name__ == "__main__":
    input = "How can I find the truth?"
    print(queryDocuments(input))
    print(queryExtractive(input))
    print(queryGenerative(input))