# 진료 길잡이 — 일본 마운자로 정보 디렉터리

도쿄·오사카·후쿠오카·삿포로·나고야·교토의 공개 안내를 정리한 한국어 정적 사이트입니다. 의료기관의 공식 사이트, 광고, 제휴 서비스가 아닙니다. 예약·진료·개인정보 입력은 받지 않습니다.

## 파일

- `index.html` — 도시별 18곳 안내. 본문은 HTML에 들어 있어 검색로봇이 JavaScript 없이도 읽을 수 있습니다.
- `support.html` — 자발적 안내. 토스뱅크 `1002-0836-8104`, 복사 버튼.
- `styles.css`, `copy.js`, `favicon.svg`
- `robots.txt`, `sitemap.xml`
- `404.html` — 없는 주소. 검색 색인 대상이 아니므로 사이트맵에 넣지 않습니다.
- `build_site.py` — 페이지를 다시 만들 때 사용. 공개 페이지는 아닙니다.
- `netlify.toml` — 정적 배포와 기본 헤더.

기관 이름, 주소, 전화, 이메일, 운영시간, 공식 링크는 첨부된 기존 파일의 문구를 유지했습니다. 없는 연락처를 채우지 않았고, 확인되지 않은 항목은 확인되지 않았다고 적었습니다.

## 주소를 바꾸는 곳

공개 주소가 정해지면 `YOUR_PUBLIC_SITE_URL` 을 슬래시 없이 바꿉니다. 예: `https://example.netlify.app`

같은 문자열이 아래 네 파일에 있습니다.

- `index.html` — canonical, Open Graph, JSON-LD
- `support.html` — canonical, Open Graph
- `robots.txt` — Sitemap
- `sitemap.xml` — 두 페이지 주소

다시 생성하려면 `build_site.py` 맨 위의 `SITE_URL` 을 바꾼 뒤 실행합니다.

```powershell
py -3 build_site.py
```

`noindex` 는 404 페이지에만 있습니다. 메인과 후원 페이지는 검색로봇 접근을 허용합니다.

## 무료 호스팅 (Netlify)

1. [Netlify](https://app.netlify.com/)에 로그인합니다.
2. [Netlify Drop](https://app.netlify.com/drop)에 이 폴더를 끌어다 놓거나, Netlify CLI에서 이 폴더를 배포합니다.
3. 발급된 `https://사이트이름.netlify.app` 주소로 위 자리표시자를 바꾼 뒤 한 번 더 배포합니다.
4. 사이트 설정에서 비밀번호 보호를 켜지 않습니다. 검색로봇이 로그인 없이 HTML을 받아야 합니다.

## 배포 전 검색로봇 점검

주소의 자리표시자를 실제 주소로 바꾼 뒤, 아래처럼 본문 HTML이 200으로 오는지 확인합니다. 로그인, 비밀번호, 보안 챌린지 페이지가 나오면 안 됩니다. 응답 본문에 기관 이름 `Nihonbashi` 가 있어야 합니다.

```powershell
curl.exe -sI -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://사이트이름.netlify.app/
curl.exe -sI -A "Mozilla/5.0 (compatible; Yeti/1.1; +https://naver.me/spd)" https://사이트이름.netlify.app/
curl.exe -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://사이트이름.netlify.app/ | findstr Nihonbashi
curl.exe -s -A "Mozilla/5.0 (compatible; Yeti/1.1; +https://naver.me/spd)" https://사이트이름.netlify.app/support.html | findstr "1002-0836-8104"
```

브라우저에서 같은 주소를 열어 도시 이동, 지도 링크, 계좌 복사도 확인합니다.

## 검색 등록

주소가 확정되고 위 점검이 끝난 뒤에만 진행합니다. 소유 확인 코드는 각 서비스가 발급합니다. 코드를 받기 전에는 넣지 않습니다.

- 구글: [Search Console](https://search.google.com/search-console)에서 속성 추가 후 HTML 파일 또는 메타 태그로 소유 확인. 사이트맵 `https://사이트이름.netlify.app/sitemap.xml` 제출.
- 네이버: [서치어드바이저](https://searchadvisor.naver.com/)에서 사이트 추가 후 HTML 메타 태그로 소유 확인. 같은 사이트맵 제출.
- 다음: [검색등록](https://register.search.daum.net/index.daum)에서 사이트 URL 신청. 웹문서 수집은 [웹마스터도구](https://webmaster.daum.net/)에서 PIN을 만든 뒤, 화면에 나온 인증 코드를 `robots.txt` 맨 아래에 붙이고 사이트맵을 수집 요청합니다.

검색 등록은 노출을 보장하지 않습니다. 검토와 수집에 며칠에서 몇 주가 걸릴 수 있습니다.
