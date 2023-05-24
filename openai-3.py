#파일 이름을 openai.py로 설정하지 말것, import openai와 혼동으로 인해 오류 발생

import openai
import os

# OpenAI API 인증키 설정
openai.api_key = os.environ["OPENAI_API_KEY"]

# 문장 생성 함수
def generate_text(prompt):
    # GPT-3 모델에 대한 요청 생성
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # 요청 결과에서 생성된 문장 반환
    return response.choices[0].text.strip()

# 문장 생성 예제
prompt = "Hello, my name is ChatGPT and I"
generated_text = generate_text(prompt)
print(generated_text)
