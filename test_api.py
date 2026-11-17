# test_api.py
import requests

API_KEY = "sk-cody-live-D_1igMWySwQ1bzWPmNBZhTA06414KFd1uRSOdcQthZ0"  # 본인의 코디세이 키

# 코디세이 Cursor 호환 엔드포인트
url = "https://copa.codyssey.kr/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY.strip()}",
    "Content-Type": "application/json",
    "User-Agent": "Cursor/0.40.0"  # 프록시가 에디터 호출만 허용할 경우를 대비한 헤더
}

# 코디세이 모델 테이블에 등록된 모델명
payload = {
    "model": "claude-sonnet-4",
    "messages": [
        {"role": "user", "content": "안녕 넌 누구니?"}
    ],
    "max_tokens": 150
}

response = requests.post(url, headers=headers, json=payload)
print("상태 코드:", response.status_code)
print("응답 내용:", response.text)