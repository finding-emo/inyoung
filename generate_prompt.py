types = {
    "강아지": "puppy with a puppy stick",
    "고양이": "cat",
    "펭귄": "penguin chick",
    "토끼": "bunny with a carrot",
    "곰": "chubby bear",
    "학생": "student wearing school uniform",
    "직장인": "businessman in a suit with a briefcase",
    "아줌마": "middle-aged female",
    "아저씨": "middle-aged male",
    "공주": "princess wearing a crown and a dress",
    "왕자": "prince wearing a crown and a cloak",
}

moods = {
    "귀여운": "cute",
    "재밌는": "witty",
    "시크한": "cynical",
    "동화 같은": "fairytale-ish",
    "사진 같은": "photograph",
    "단순한": "simple, minimal",
    "못생긴": "ugly",
}

colors = {
    "흑백": "monochrome",
    "비비드": "vivid color scheme",
    "파스텔": "pastel color scheme",
}


def generate_prompt(
    keywords: list,
    emotions: list,
    gestures: list,
    type: str,
    mood: str,
    color: str,
):
    # 인풋으로 models()함수의 출력으로 나온 딕셔너리형 extracted_keywords를 받게 됨.

    prompts = []  # 그림 여러개 출력할 것이므로 이 리스트에 담아둘 것.

    keyword = " and ".join(keywords)
    emotion = " and ".join(emotions)
    gesture = " and ".join(gestures)

    styles = ("a chat emoji with a", "an illustration of a", "a")

    for style in styles:
        prompt = f"""
{style} {types[type]},
with a {moods[mood]} mood,
in {colors[color]},
in a situation about {keyword},
expressing emotions involving {emotion},
with gestures or facial expressions {gesture}
"""

        prompts.append(prompt)

    negative_prompt = """
any kind of text,
word,
body out of frame,
out of frame,
bad anatomy,
distortion,
disfigured,
poorly drawn face,
poorly drawn hands,
low quality,
low contrast,
draft,
amateur,
cut off,
cropped"""

    return (prompts, negative_prompt)
