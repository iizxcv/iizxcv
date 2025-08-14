import sys
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

multitap = []
cnt = 0

for i in range(k):
    if lst[i] in multitap:
        continue
    if len(multitap) < n:
        multitap.append(lst[i])
    else:
        # 앞으로 사용되지 않는 기기 제거 우선
        remove_candidate = -1
        latest_use = -1
        for tap in multitap:
            if tap not in lst[i:]:
                remove_candidate = tap
                break
            else:
                idx = lst[i:].index(tap)
                if idx > latest_use:
                    latest_use = idx
                    remove_candidate = tap
        multitap.remove(remove_candidate)
        cnt += 1
        multitap.append(lst[i])

print(cnt)

# ✅ 최종 결론
# 항목	판단
# 로직상 문제	❌ 없음
# 알고리즘 그리디 전략 구현	✅ 정답
# 실패 원인	⚠️ 리스트 순회 중 .remove()로 인한 비정상 흐름 가능성
# 백준 오답 판정 사유	✅ 비정상적인 리스트 순회 때문
# 해결 방법	✅ .remove() 시 리스트 복사본 순회 또는 인덱스 추적 방식
# 🎯 요약
# 당신 코드의 로직은 정답이지만, 파이썬의 리스트 처리 방식상 실수할 수 있는 위험이 숨어 있습니다.
# 따라서 백준에서는 불특정 테스트케이스에서 틀렸습니다가 발생할 수 있습니다.
# 복사본을 순회하거나 구조를 살짝 바꾸면 100% 통과합니다.

# 필요하다면 당신 코드 스타일을 최대한 유지하면서 안전하게 수정된 버전도 드릴 수 있어요.




# 선택된 파일 없음선택된 파일 없음
# ChatGPT는 실수를 할 수 있습니다. 중요한 정보는 재차 확인하세요.
