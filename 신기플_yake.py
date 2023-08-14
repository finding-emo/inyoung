# %%
# !pip install yake


# %%
# !pip install konlpy
from konlpy.tag import Kkma
from konlpy.tag import Okt

okt = Okt()
kkma = Kkma()

# %%
import yake
from time import time
from konlpy.tag import Okt

okt = Okt()

language = "ko"
max_ngram_size = 1
deduplication_threshold = 0.9
deduplication_algo = "lev"
windowSize = 1
numOfKeywords = 3

all_elements = [
    "미하하하하하하하하하하하하하하하하하하하하하하하하하하하하핳ㅎㅎㅎㅎㅎㅎ",
    "나꿍꼬또댜기꿍꼬또",
    "그냥 자라..누구냐너",
    "어디 갔다 왐수꽈?",
    "요새 어떵 살미꽈? 좋수과?",
    "당연이 줄 수 있지, 문자 한번 다시 다오~^^",
    "우리가 현준이를 종잡을 수 있겠나",
    "고대 연구실에서 나올리가…",
    "다들 곧 퇴근하시겠군요",
    "재택과 백수 앞에 무력하네요",
    "짐 놓고 와도 도착하는ㅅ ㅣ간 아님?",
    "9시에 만난다고하먀ㅏㄴ 난장판 되어있을듯 하다",
    "오랜만이야~ 보고싶었어~ 나도 요새 취준해… 너도 잘 살지?",
    "난 교내 학회에서 프로젝트 하고 있는데 팀원을 때문에 너무 힘들다!!!!",
    "나도 요새 수업 듣는데 좀 힘들다ㅠㅠㅠㅠ 무려 21학점 들어야 해… 살려줘ㅠㅠ 죽고싶어ㅠㅠㅠㅠㅋㅋㅋ",
    "나 요새 마라탕 자주 먹는데 개마싰음. 나중에 시간 되면 같이 먹으러 ㄱ?",
    "엄마 나 용돈 떨어졌어 용돈 제바류ㅠㅠㅠㅠㅠ",
    "여기에 각자 5개씩 제안해주시면 감사드리겠습니다 ㅎㅎ",
    "내일까지 10분 내외로 간단하게 해당 주제에 대한 설명(주제 소개, 목표, 데이터셋, 플로우 등)을 준비해주시면 됩니다",
    "30분에맞춰서 도착할듯?",
    "그럼 일단 방먹에서봐?",
    "이것대로 인스턴스 설정하고 활성화 해야 해",
    "나 진짜 너무 배고파",
    "헐~ ㅁㅊ 그럼 어케 되는겨?",
    "오키 그럼 내일 5시에 빨잠에서 보는걸루?",
    "저는 아아로 부탁드립니다~",
    "잘자구 내일 보쟈잉!",
    "엥 ㅁㅊ 어떻게 그럴 수 있음???",
    "아 가보자고",
    "어케 해야 하는지 감이 오는 것 같음",
    "ㅇㅎ…..오비맥주도 저기 겅ㅅ구나……? 흥ㅁ로구먼",
]
start_time = time()

for text in all_elements:
    # 품사 고려 안 하기로 함, 어절 단위로만 추출하자!
    # Tag words by parts of speech and filter only nouns, adjectives, and verbs
    # pos_tags = ["Noun", "Adjective", "Verb"]
    # filtered_words = [word for word, tag in okt.pos(text) if tag in pos_tags]

    # filtered_text = " ".join(filtered_words)

    custom_kw_extractor = yake.KeywordExtractor(
        lan=language,
        n=max_ngram_size,
        dedupLim=deduplication_threshold,
        dedupFunc=deduplication_algo,
        windowsSize=windowSize,
        top=numOfKeywords,
        features=None,
    )
    keywords = custom_kw_extractor.extract_keywords(text)

    print(f"Keywords for text: '{text}'")
    for kw, score in keywords:  # lower the score, more relevant the keyword
        tag = None
        for word, tag_ in okt.pos(
            kw
        ):  # Corrected the loop for unpacking word-tag pairs
            if kw == word:
                tag = tag_
                break
        print(f"{kw} (Score: {score:.4f})")
    print("\n")

end_time = time()
running_time = end_time - start_time

print("model running time: %s " % f"{running_time:12.9f}", end="")

# %%
# 조사, 어미 제외한 버전

import yake
import re
from time import time
from konlpy.tag import Okt

okt = Okt()

language = "ko"
max_ngram_size = 1
deduplication_threshold = 0.9
deduplication_algo = "lev"
windowSize = 1
numOfKeywords = 3

weight_mapping = {"Noun": 1.5, "Verb": 1.2, "Adjective": 1.2}

punctuations = {
    ",",
    ".",
    ":",
    ";",
    "?",
    "!",
    "#",
    "&",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    "|",
    "\\",
    "/",
    "<",
    ">",
    "~",
    "`",
    "@",
    "$",
    "%",
    "^",
    "*",
    "[SEP]",
    "[CLS]",
    '"',
}


def tokenize_with_punctuations(text):
    for p in punctuations:
        text = text.replace(p, " ")
    return text.split()


all_elements = [
    "미하하하하하하하하하하하하하하하하하하하하하하하하하하하하핳ㅎㅎㅎㅎㅎㅎ",
    "나꿍꼬또댜기꿍꼬또",
    "그냥 자라..누구냐너",
    "어디 갔다 왐수꽈?",
    "요새 어떵 살미꽈? 좋수과?",
    "당연이 줄 수 있지, 문자 한번 다시 다오~^^",
    "우리가 현준이를 종잡을 수 있겠나",
    "고대 연구실에서 나올리가…",
    "다들 곧 퇴근하시겠군요",
    "재택과 백수 앞에 무력하네요",
    "짐 놓고 와도 도착하는ㅅ ㅣ간 아님?",
    "9시에 만난다고하먀ㅏㄴ 난장판 되어있을듯 하다",
    "오랜만이야~ 보고싶었어~ 나도 요새 취준해… 너도 잘 살지?",
    "난 교내 학회에서 프로젝트 하고 있는데 팀원을 때문에 너무 힘들다!!!!",
    "나도 요새 수업 듣는데 좀 힘들다ㅠㅠㅠㅠ 무려 21학점 들어야 해… 살려줘ㅠㅠ 죽고싶어ㅠㅠㅠㅠㅋㅋㅋ",
    "나 요새 마라탕 자주 먹는데 개마싰음. 나중에 시간 되면 같이 먹으러 ㄱ?",
    "엄마 나 용돈 떨어졌어 용돈 제바류ㅠㅠㅠㅠㅠ",
    "여기에 각자 5개씩 제안해주시면 감사드리겠습니다 ㅎㅎ",
    "내일까지 10분 내외로 간단하게 해당 주제에 대한 설명(주제 소개, 목표, 데이터셋, 플로우 등)을 준비해주시면 됩니다",
    "30분에맞춰서 도착할듯?",
    "그럼 일단 방먹에서봐?",
    "이것대로 인스턴스 설정하고 활성화 해야 해",
    "나 진짜 너무 배고파",
    "헐~ ㅁㅊ 그럼 어케 되는겨?",
    "오키 그럼 내일 5시에 빨잠에서 보는걸루?",
    "저는 아아로 부탁드립니다~",
    "잘자구 내일 보쟈잉!",
    "엥 ㅁㅊ 어떻게 그럴 수 있음???",
    "아 가보자고",
    "어케 해야 하는지 감이 오는 것 같음",
    "ㅇㅎ…..오비맥주도 저기 겅ㅅ구나……? 흥ㅁ로구먼",
]


start_time = time()

for text in all_elements:
    tokenized_words = tokenize_with_punctuations(text)

    # pos_tags = ["Noun", "Adjective", "Verb"]
    filtered_words = []

    # Use konlpy to filter out particles and endings
    for word, tag in okt.pos(" ".join(tokenized_words)):
        if tag not in ["Josa", "Eomi"]:
            filtered_words.append(word)

    filtered_text = " ".join(filtered_words)

    custom_kw_extractor = yake.KeywordExtractor(
        lan=language,
        n=max_ngram_size,
        dedupLim=deduplication_threshold,
        dedupFunc=deduplication_algo,
        windowsSize=windowSize,
        top=numOfKeywords,
        features=None,
    )
    keywords = custom_kw_extractor.extract_keywords(filtered_text)

    print(f"Keywords for text: '{text}'")
    for kw, score in keywords:
        tag = None
        for word, tag_ in okt.pos(kw):
            if kw == word:
                tag = tag_
                break
        print(f"{kw} (Score: {score:.4f})")
    print("\n")

end_time = time()
running_time = end_time - start_time

print("model running time: %s " % f"{running_time:12.9f}", end="")
