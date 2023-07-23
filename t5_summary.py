from langchain import HuggingFaceHub, PromptTemplate

from config import Config


llm = HuggingFaceHub(
    repo_id=Config.LLM_MODEL_NAME,
    huggingfacehub_api_token=Config.HUGGINGFACEHUB_API_TOKEN,
    model_kwargs={'temperature': Config.LLM_TEMPERATURE, 'max_length': Config.LLM_MAX_OUTPUT_LENGTH}
)
# print(llm)

template = '''
You are a helpful assistant who can review literature and poetry.
A poem consists of one or more stanzas. A stanza may contain as few as a single line. 
Consecutive stanzas are separated by blank lines. Generally, the stanzas stand out differently.
Consider the following poem: 

{poem}


Write a creative summary of the poem in about 20 words. 
The summary should try to capture the subjects, objects, key themes, and sentiments.
The summary should avoid verbatim use of lines from the poem.
'''

prompt = PromptTemplate.from_template(template)


def generate_summary(poem: str) -> str:
    """
    Generate the summary of a poem using an LLM.

    :param poem: The text of the poem
    :return: The summary
    """

    print(prompt.format(poem=poem))
    summary = llm(prompt.format(poem=poem))

    return summary
