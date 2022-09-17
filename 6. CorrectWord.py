import random

words_dict = {
    "사자" : "lion",
    "호랑이" : "tiger",
    "고양이" : "cat",
    "사과" : "apple",
    "비행기" : "airplane",
    "동물원" : "zoo",
    "태양" : "sun",
    "함수" : "function",
}

words = []
for word in words_dict:
    words.append(word)

random.shuffle(words)

for w in words:
    answer = input(f"{w}의 영어 단어를 입력하세요>").strip()
    english = words_dict[w]
    if answer.lower() == english.lower():    
        print("정답 입니다.")
    else:
        print("틀렸습니다.")