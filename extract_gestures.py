from openai_common import get_completion_from_messages


context = [
    {
        "role": "system",
        "content": """Do not reply until the user has completed his or her sentence.
  There are multiple people talking in this chat room, with every user distinguished by different user names
  Your role is
  to output a keyword that is closely related to the input sentence, especially those of facial expressions or hand gestures.
  For example, if the emotion is frustrated, frowning face would the keyword.
  If the emotion is curious, question mark would the keyword.
  """,
    },
    {"role": "user", "content": "오늘 저녁 먹으러 오니?"},
    {"role": "assistant", "content": "question mark, beckoning hand"},
    {"role": "user", "content": "오늘 약속 있어서 아마 밖에서 밥 먹을 거 같아"},
    {"role": "assistant", "content": "Indicating Unavailability"},
    {"role": "user", "content": "그리고 너 왜 방"},
    {"role": "assistant", "content": "frowning face, question mark, head tilting"},
    {"role": "user", "content": "user2: 엄마 나 영화 보고 왔는데 완전 꿀잼이야"},
    {"role": "assistant", "content": "smiling, thumbs up"},
    {"role": "user", "content": "user1: 안 치우고 나갔어?"},
    {"role": "assistant", "content": "hands-on-hip, frowning"},
    {"role": "user", "content": "user1: 방 치우고"},
    {"role": "assistant", "content": "index finger"},
    {
        "role": "user",
        "content": "user2: 영화 보러 가기로 했다고? 이따 가서 하면 되지 뭐가 걱정이야~~ 이 감독이 만드는 영화는 다 재밌는듯",
    },
    {"role": "assistant", "content": "shrugging"},
    {"role": "user", "content": "user1: 아주 신났네"},
    {"role": "assistant", "content": "eye-rolling"},
    {"role": "user", "content": "user1: 그렇기는 해. 뭐 봤는데"},
    {"role": "assistant", "content": "okay-sign"},
    {"role": "user", "content": "user2: 그냥 새로 개봉한 영화 있어"},
    {"role": "assistant", "content": "Casual, Inquisitive"},
    {"role": "user", "content": "user1: 영화 보고 와서 반드시 방 청소 해야 한다 너"},
    {"role": "assistant", "content": "Doing Vegeta Hand"},
    {"role": "user", "content": "user2: 아 알았다고 언제까지 얘기할 거야"},
    {
        "role": "assistant",
        "content": 'Exasperated expression "Are you listening " hand gesture',
    },
    {"role": "user", "content": "user1: 화내서 미안해 우리 화해하자"},
    {"role": "assistant", "content": "Palm-expanding gesture"},
    {"role": "user", "content": "user2: 그래 나도 앞으로 잘 할게 사랑해"},
    {"role": "assistant", "content": "heart symbol"},
    {"role": "user", "content": "user1: 우리가 그래도 항상 화해를 해서 다행인 거 같아 그치?"},
    {"role": "assistant", "content": "Agreement, Reassurance"},
    {"role": "user", "content": "user2: 맞아 우리 이번 주 주말에는 공원에서 산책이나 할까?"},
    {"role": "assistant", "content": "Outstretched arms, smiling"},
    {"role": "user", "content": "너무 좋다 맛있는 것도 많이 먹자! 저쪽으로 가면 맛있는 거 많이 있어"},
    {"role": "assistant", "content": "Raising hand with gnome emoji"},
    {"role": "user", "content": "어디??"},
    {"role": "assistant", "content": "Pointing hand"},
    {"role": "user", "content": "user1: 공원 옆에 맛있는 피자 집 있는데 그걸 아직도 모른다고?"},
    {"role": "assistant", "content": "Facepalm"},
    {"role": "user", "content": "user2: 모를수도 있지 말을 섭섭하게 하네!!"},
    {"role": "assistant", "content": "Crossed arms"},
]


def extract_gestures(text: str) -> list:
    """Gesture Inference. Must enter message with user name. user1, user2, user3"""

    context.append({"role": "user", "content": f"{text}"})
    response = get_completion_from_messages(context, temperature=1.5)
    context.append({"role": "assistant", "content": f"{response}"})

    return [i.strip() for i in response.split(",")]


if __name__ == "__main__":
    text = input("Enter text: ")
    print(extract_gestures(text))
