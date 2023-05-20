
# from haystack.pipelines import ExtractiveQAPipeline, DocumentSearchPipeline, GenerativeQAPipeline
from shared import retriever #, reader, generator

# querying_pipeline = ExtractiveQAPipeline(reader, retriever)
# generative_pipeline = GenerativeQAPipeline(generator, retriever)
# search_pipe = DocumentSearchPipeline(retriever)
# params = {
#     "Retriever": {"top_k": 5},
# }

def queryDocuments(input):
    return {}
    # answer = search_pipe.run(
    #     query=input,
    #     params=params
    # )
    # return answer
def queryExtractive(input):
    return {}
    # answer = querying_pipeline.run(
    #     query=input,
    #     params=params
    # )
    # return answer
def queryGenerative(input):
    return {}
    # answer = generative_pipeline.run(
    #     query=input,
    #     params=params
    # )
    # return answer

if __name__ == "__main__":
    input = "How can I find the truth?"
    print(queryDocuments(input))
    print(queryExtractive(input))
    print(queryGenerative(input))