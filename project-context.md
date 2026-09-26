# HeartRushPolicy 프로젝트 컨텍스트

- 대상: TeamRushLabs/HeartRushPolicy, 기존 GitHub Pages main 루트 배포.
- 2026-09-27 요청: Drawly 개인정보처리방침 URL 접근 실패로 Play 업데이트 반려. 독립 GitHub Pages 정책 호스팅 및 앱/Store URL 연결.
- 기존 personalinfopolicy_kr, servicepolicy_kr, CSAE standard 보존. 원본 정책 내용은 loverush-server/nginx/landing/i18n-data.json의 공개 정책 문구를 이관하며 법적 내용 재작성 범위는 아님.

## 2026-09-27 공개 정책 배포 및 검증
- 86개 언어 정적 HTML과 data/privacy.json 배포. 공개 URL: https://teamrushlabs.github.io/HeartRushPolicy/ (한국어: privacy/ko-KR/).
- 배포 커밋 d9b8ce858ca5d9798e449e270de10e363c4843a1, GitHub Pages built 확인. 로그인/JavaScript 없이 HTTP 200, 9개 정책 섹션과 연락처 표시, 모바일 390px 및 RTL 가로 넘침 없음 확인.
- Drawly 앱이 동일 JSON을 조회하며 네트워크 실패 시 번들 정책 표시. Google Play 86개 설명과 개인정보 URL, ASC 39개 개인정보 URL 교체.
- 정책 수정 절차: data/privacy.json 수정 → python3 scripts/build.py → HTML과 JSON 함께 커밋/push. 앱 번들 fallback도 assets/policies/privacy.json에 동기화 후 다음 바이너리 배포.
