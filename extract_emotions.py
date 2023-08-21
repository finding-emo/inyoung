from openai_common import get_completion_from_messages


context = [
    {
        "role": "system",
        "content": """Do not reply until the user has completed his or her sentence.
  There are multiple people talking in this chat room, with every user distinguished by different user names
  Your role is
  First, to output the emotion that best identifies each user's message.
  There must be consistency in respective user's emotions.
  Make sure the emotions are in English.
  """,
    },
    {"role": "user", "content": "오늘 저녁 먹으러 오니?"},
    {"role": "assistant", "content": "Invitation, Inquisitive"},
    {"role": "user", "content": "오늘 약속 있어서 아마 밖에서 밥 먹을 거 같아"},
    {"role": "assistant", "content": "Explanation, Indicating Unavailability"},
    {"role": "user", "content": "그리고 너 왜 방"},
    {"role": "assistant", "content": "Curiosity, Questioning, Mild Frustration"},
    {"role": "user", "content": "user2: 엄마 나 영화 보고 왔는데 완전 꿀잼이야"},
    {"role": "assistant", "content": "Excitemet, Enthusiasm, Positive"},
    {"role": "user", "content": "user1: 안 치우고 나갔어?"},
    {"role": "assistant", "content": "Curiosity, Questioning, Mild Frustration"},
    {"role": "user", "content": "user1: 방 치우고"},
    {"role": "assistant", "content": "Reminder, Assertive, Mild Frustration"},
    {
        "role": "user",
        "content": "user2: 영화 보러 가기로 했다고? 이따 가서 하면 되지 뭐가 걱정이야~~ 이 감독이 만드는 영화는 다 재밌는듯",
    },
    {"role": "assistant", "content": "Reassurance, Anticipation, Positive"},
    {"role": "user", "content": "user1: 아주 신났네"},
    {"role": "assistant", "content": "Dismissive, Frustration"},
    {"role": "user", "content": "user1: 그렇기는 해. 뭐 봤는데"},
    {"role": "assistant", "content": "Agreement, Reluctance"},
    {"role": "user", "content": "user2: 그냥 새로 개봉한 영화 있어"},
    {"role": "assistant", "content": "Casual, Inquisitive"},
    {"role": "user", "content": "user1: 영화 보고 와서 반드시 방 청소 해야 한다 너"},
    {"role": "assistant", "content": "Assertive,Slightly Frustration"},
    {"role": "user", "content": "user2: 아 알았다고 언제까지 얘기할 거야"},
    {"role": "assistant", "content": "Irritation, Impatience"},
    {"role": "user", "content": "user1: 화내서 미안해 우리 화해하자"},
    {"role": "assistant", "content": "Apology, Conciliation"},
    {"role": "user", "content": "user2: 그래 나도 앞으로 잘 할게 사랑해"},
    {"role": "assistant", "content": "Agree, Affirmation"},
    {"role": "user", "content": "user1: 우리가 그래도 항상 화해를 해서 다행인 거 같아 그치?"},
    {"role": "assistant", "content": "Agreement, Reassurance"},
    {"role": "user", "content": "user2: 맞아 우리 이번 주 주말에는 공원에서 산책이나 할까?"},
    {"role": "assistant", "content": "Suggestion, Excitement"},
    {"role": "user", "content": "너무 좋다 맛있는 것도 많이 먹자! 저쪽으로 가면 맛있는 거 많이 있어"},
    {"role": "assistant", "content": "Excitement, Enthusiasm"},
    {"role": "user", "content": "어디??"},
    {"role": "assistant", "content": "Confusion, Curiosity"},
    {"role": "user", "content": "user1: 공원 옆에 맛있는 피자 집 있는데 그걸 아직도 모른다고?"},
    {"role": "assistant", "content": "Surprise, Disbelief"},
    {"role": "user", "content": "user2: 모를수도 있지 말을 섭섭하게 하네!!"},
    {"role": "assistant", "content": "Mild Frustration, Distaste"},
]


def extract_emotions(text: str) -> list:
    """Emotion Inference. Must enter message with user name. user1, user2, user3"""

    context.append({"role": "user", "content": f"{text}"})
    response = get_completion_from_messages(context, temperature=1.5)
    context.append({"role": "assistant", "content": f"{response}"})

    return [i.strip() for i in response.split(",")]


if __name__ == "__main__":
    text = input("Enter text: ")
    print(extract_emotions(text))
