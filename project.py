import pandas as pd
import Levenshtein

class SimpleChatBot:
    def __init__(self, filepath):
        # CSV 파일 읽기
        self.chatbot = pd.read_csv(filepath)
    
    def Leven_distance(self, input_sentence):
        # 레벤슈타인 거리 계산
        self.chatbot['Levenshtein_Distance'] = self.chatbot['Q'].apply(lambda x: Levenshtein.distance(x, input_sentence))
        # 가장 유사한 질문의 인덱스 찾기
        min_distance_index = self.chatbot['Levenshtein_Distance'].idxmin()
        return min_distance_index

# CSV파일 위치
filepath = './ChatbotData.csv' 
chatbot = SimpleChatBot(filepath)

while True:
    # 질문
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    # 입력 문장과 가장 유사한 질문의 인덱스 찾기
    response_index = chatbot.Leven_distance(input_sentence)
    print('Index:', response_index)

    # 해당 인덱스의 답변 출력
    response_answer = chatbot.chatbot.loc[response_index, 'A']
    print('Chatbot: A:', response_answer)
    
