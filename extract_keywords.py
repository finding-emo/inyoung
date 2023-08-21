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


def extract_keywords(text: str) -> list:
    """
    Keyword extraction

    ``text``: ``str`` type. The text to be processed.

    ``return``: ``list[dict[str, object]]`` type.
    The list of extracted keywords and their scores.
    The higher the score, the more relevant the keyword.
    """
    keywords = custom_kw_extractor.extract_keywords(text)

    extracted_keywords = [
        {
            "keyword": kw,
            "score": 1 - score,
        }
        for kw, score in keywords
    ]

    return extracted_keywords


if __name__ == "__main__":
    text = input("Enter text: ")
    print(extract_keywords(text))
