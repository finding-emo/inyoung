import yake

language = "ko"
max_ngram_size = 1
deduplication_threshold = 0.9
deduplication_algo = "lev"
windowSize = 1
numOfKeywords = 3

custom_kw_extractor = yake.KeywordExtractor(
    lan=language,
    n=max_ngram_size,
    dedupLim=deduplication_threshold,
    dedupFunc=deduplication_algo,
    windowsSize=windowSize,
    top=numOfKeywords,
    features=None,
)

import openai
# import os

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
# openai.api_key  = os.getenv(key)

openai.api_key  = ''

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

context =  [  
{'role':'system', 'content':'''Do not reply until the user has completed his or her sentence.
There are multiple people talking in this chat room, with every user distinguished by different user names
Your role is to output the emotion that best identifies each user's message.
There must be consistency in respective user's emotions.
Make sure the emotions are in English'''}, 

{'role':'user', 'content':'user1: 너를 체포하겠어!'},   
{'role':'assistant', 'content':'Anger, Threatening'},

{'role':'user', 'content':'user1: 내 마음을 훔친 죄로 너를 체포하겠다구!'},
{'role':'assistant', 'content':'Playful Teasing'},

{'role': 'user', 'content': 'user1: 나 오늘'},
{'role': 'assistant', 'content': 'Eagerness'},

{'role': 'user', 'content': 'user1: 꿍꼬또 귀신 꿍꼬또'},
{'role': 'assistant', 'content': 'Playful Excitement'},

{'role': 'user', 'content': 'user1: 그래서 말인데'},
{'role': 'assistant', 'content': 'Cautious Expectation'},

{'role': 'user', 'content': 'user1: 오늘 나랑 같이 자면 안될까~?'},
{'role': 'assistant', 'content': 'Surprise'},

{'role': 'user', 'content': 'user1: 그러면 너무 좋겠당ㅎㅎ'},
{'role': 'assistant', 'content': 'Happiness'},

{'role':'user', 'content':'user2: 오늘 저녁 먹으러 오니?'},  
{'role':'assistant', 'content': 'Invitation, Inquisitive'},

{'role':'user', 'content':'user1: 오늘 약속 있어서 아마 밖에서 밥 먹을 거 같아'},
{'role':'assistant', 'content':'Explanation, Indicating Unavailability'}
] 


def model(text: str) -> list:
    """
    Keyword Extraction
    ``text``: ``str`` type. The text to be processed.

    ``return``: ``list[dict[str, object]]`` type.
    The list of extracted keywords and their scores.
    The higher the score, the more relevant the keyword.
    
    """
    keywords = custom_kw_extractor.extract_keywords(text)
    
    
    """Emotion Inferenc. Must enter message with user name. user1, user2, user3"""
    
    context.append({'role':'user', 'content':f"{text}"})
    response = get_completion_from_messages(context, temperature=1.5)
    context.append({'role':'assistant', 'content':f"{response}"})
    
    extracted_keywords = [
        {
            "keyword": kw,
            "score": 1 - score,
        }
        for kw, score in keywords
        ]
    extracted_keywords.append({ "emotion": [i.strip() for i in response.split(",")]})

    return extracted_keywords

if __name__ == "__main__":
    text = input("text 입력: ")
    print(model(text))
