import yake
from time import time

def model(prompt: str) -> list:
    """
    ``prompt``: ``str`` type. The prompt to be processed.

    ``return``: ``list[dict[str, object]]`` type.
    The list of extracted keywords and their scores.
    The higher the score, the more relevant the keyword.
    """

    language = "ko"
    max_ngram_size = 1
    deduplication_threshold = 0.9
    deduplication_algo = 'lev'
    windowSize = 1
    numOfKeywords = 3

    custom_kw_extractor = yake.KeywordExtractor(lan=language,
                                                n=max_ngram_size,
                                                dedupLim=deduplication_threshold,
                                                dedupFunc=deduplication_algo,
                                                windowsSize=windowSize,
                                                top=numOfKeywords,
                                                features=None)
    keywords = custom_kw_extractor.extract_keywords(prompt)

    extracted_keywords = [
        {
            "keyword": kw,
            "score": score,
        }
        for kw, score in keywords
    ]

    return extracted_keywords

"""
    return [
        {
            "keyword": "아침",
            "score": 0.6,
        },
        {
            "keyword": "먹다",
            "score": 0.4,
        },
    ]
"""
