def model(prompt: str) -> list:
    """
    ``prompt``: ``str`` type. The prompt to be processed.

    ``return``: ``list[dict[str, object]]`` type.
    The list of extracted keywords and their scores.
    The higher the score, the more relevant the keyword.
    """

    # TODO: Implement your model here.

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
