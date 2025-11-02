import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="경영학전공 1문 1답",
    page_icon="🎓",
    layout="wide"
)

# D-ID Agent - st.html() 사용
st.html("""
<script type="module">
(function() {
    const script = document.createElement('script');
    script.type = 'module';
    script.src = 'https://agent.d-id.com/v2/index.js';
    script.setAttribute('data-mode', 'fabio');
    script.setAttribute('data-client-key', 'Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll');
    script.setAttribute('data-agent-id', 'v2_agt_80jV_9EA');
    script.setAttribute('data-name', 'did-agent');
    script.setAttribute('data-monitor', 'true');
    script.setAttribute('data-orientation', 'horizontal');
    script.setAttribute('data-position', 'right');
    document.body.appendChild(script);
})();
</script>
""")

# 제목
st.title("🎓 경영학전공 1문 1답")
st.caption("미래융합대학 헬스케어융합학부 | 박대근 교수")

# 14개 탭 구성
tabs = st.tabs([
    "연구분야", "통합교육", "취업전망", "세부전공", "미래가치", 
    "팀프로젝트", "바이오융합", "차대만의강점", "졸업생진로", 
    "예술경영", "디지털vs AI", "미디어융합", "수포자OK", "영상광고"
])

with tabs[0]:
    st.header("🔬 경영학전공에서는 실제로 어떤 연구들을 다루나요?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 연구 분야")
        st.info("""
        **경영학 핵심 이론**
        - 경영기획: 기업전략, 조직관리 등 
        - 마케팅: 소비자 행동, 브랜드 전략, 서비스 마케팅 등 
        - 회계재무: 기업가치 평가, 회계투명성, 투자의사결정 등 
        
        **최신 트렌드**
        - 경영기획: ESG 평가지표 개발, 기업지배구조 개선
        - 마케팅: AI 서비스 로봇 수용도, MZ세대 SNS 전략
        - 회계재무: 제약·바이오 R&D 회계처리, 공시정보 신뢰성
        """)
        
    with col2:
        st.subheader("🏆 교수진 연구 성과")
        st.success("""
        **국내외 저널 게재**
        - 국제: Psychology & Marketing | Applied Economics Letters | Journal of Forecasting | International Journal of Hospitality Management | Journal of Vacation Marketing | International Journal of Tourism Research
        - 국내: 회계학연구 | 경영학연구 | 한국언론학보 | 한국방송학보 | 고객만족경영연구 | 상품학연구 | 경영과학회지 | 회계저널
                    
        **주요 연구 주제**
        - 경영기획: ESG 뉴스의 기업가치 영향 분석 등 
        - 마케팅: K-콘텐츠의 글로벌 시장 전략, 디지털 리터러시와 소비자 참여 등 
        - 회계재무: 주주권 행사와 이익조정, 신용평가와 재무보고 적시성 등 
        - 융합분야: AI융합연구방법론, AI를 활용한 시계열 예측, AI 지능형 봇 개발 등  
        """)

with tabs[1]:
    st.header("🤝 왜 마케팅이나 인사관리 같은 수업도 들어야 하나요?")
    
    st.warning("💡 **기업 경영 = 퍼즐 맞추기**: 한 조각만으로는 전체 그림을 볼 수 없어요!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **재무 전문가도**
        - 신규 사업 시장성 평가
        - 마케팅 ROI 분석
        - 투자 타당성 검토
        """)
    
    with col2:
        st.success("""
        **회계사도**
        - 인건비 구조 이해
        - 원가 구조 분석
        - 부서별 예산 검토
        """)
    
    with col3:
        st.error("""
        **실무 협업**
        - 재무팀 ↔ 마케팅팀
        - 전략팀 ↔ 운영팀
        - 크로스펑션 프로젝트
        """)
    
    st.subheader("🎯 통합 교육 프로그램")
    st.write("""
    - **액션러닝**: 실제 기업 문제 해결
    - **케이스스터디**: 나이키, 삼성 등 실제 사례 분석
    - **협력기관**: 한국조세재정연구원, 국회예산정책처, 금융감독원
    """)

with tabs[2]:
    st.header("💼 경영학만 전공해도 취업이 되나요?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.metric("취업률", "88.7%", "전국 평균 대비 우수")
        
        st.subheader("📊 직무별 진출 현황")
        st.progress(49, text="경영기획 48.9%")
        st.progress(21, text="회계세무금융 20.8%")
        st.progress(14, text="마케팅 14.0%")
        
    with col2:
        st.subheader("🏢 기업 규모별")
        st.info("""
        - **중소기업**: 30.8%
        - **외감기업**: 19.5%
        - **코스피**: 8.1%
        - **코스닥**: 6.3%
        """)
    
    st.success("""
    ✅ **경영학 단일전공만으로도 충분!**
    - 다양한 산업 진출 가능
    - 복수전공은 차별화 전략 (선택사항)
    - 스포츠의학 복수전공 시 78조원 스포츠산업 진출 유리
    """)

with tabs[3]:
    st.header("📚 경영학 안에도 세부 전공이 있나요?")
    
    st.subheader("6대 주요 분야")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **🎯 경영기획**
        - 기업 전략 수립
        - 조직 설계
        - ESG 경영
        - 진로: 전략기획, 경영컨설팅
        """)
        
    with col2:
        st.info("""
        **📈 마케팅**
        - 소비자 행동 분석
        - 브랜드 관리
        - 디지털 마케팅
        - 진로: 마케팅매니저, 브랜드매니저
        """)
        
    with col3:
        st.info("""
        **💰 회계재무**
        - 재무제표 분석
        - 투자 의사결정
        - 리스크 관리
        - 진로: 회계사, 애널리스트, 펀드매니저
        """)

    st.subheader("🏥 차의과학대 특화 분야")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **헬스케어 비즈니스**
        - 의료서비스 경영
        - 의료관광
        - 바이오산업 분석
        """)
    
    with col2:
        st.success("""
        **비즈니스 애널리틱스**
        - 경영빅데이터 분석
        - 건강보험공단 데이터 활용
        - AI 기반 의사결정
        """)

with tabs[4]:
    st.header("🔮 경영학이 미래에도 여전히 중요할까요?")
    
    st.error("🚀 **오히려 더 중요해집니다!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("AI 시대에도 필요한 이유")
        st.info("""
        **기술 ≠ 비즈니스**
        - AI/빅데이터를 비즈니스로 전환
        - 기술 이해 + 사업모델 설계
        - 인간 중심 가치 창출
        
        **경영 전문가 역할**
        - 전략적 의사결정
        - 이해관계자 조정
        - 윤리적 경영 판단
        """)
    
    with col2:
        st.subheader("미래 대비 연구")
        st.success("""
        **최신 연구 주제**
        - 생성형 AI 활용 ESG 분석
        - 디지털 전환 시대 소비자 행동
        - 헬스케어 디지털 혁신
        
        **실제 현황**
        - 미국 의료시스템 92% 디지털 혁신 추진
        - AI 기반 경영 의사결정 확산
        - ESG 경영 의무화 추세
        """)
    
    st.warning("""
    📍 **경영학의 보편성**
    - 기업, 병원, 학교, NGO 모든 조직 적용 가능
    - 창업부터 대기업까지 필수 지식
    - 미래 헬스케어 리더 양성 목표
    """)

with tabs[5]:
    st.header("👥 경영학과는 팀플이 많다고 하던데, 정말인가요?")
    
    st.success("✅ **맞아요! 팀플과 발표가 많습니다**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤔 왜 팀플이 많을까?")
        st.info("""
        **현실 반영**
        - 실제 기업 = 팀워크
        - 크로스펑션 협업 필수
        - 프로젝트 기반 업무
        
        **성공 사례**
        - 영화감독 + 프로듀서
        - 창업가 + 공동창업팀
        - CEO + 경영진
        """)
    
    with col2:
        st.subheader("🎯 팀플을 통해 얻는 것")
        st.warning("""
        **핵심 역량 개발**
        - 의사소통 능력 ↗️
        - 문제해결 능력 ↗️
        - 리더십 & 팔로워십 ↗️
        - 프레젠테이션 스킬 ↗️
        
        **실전 경험**
        - 기업경영사례 경진대회
        - 액션러닝 프로젝트
        - 취업 시 큰 강점
        """)
    
    st.error("💡 **교수님 Tip**: 자기주도적 액션러닝으로 현장 문제 해결 능력을 기릅니다!")

with tabs[6]:
    st.header("🧬 바이오나 의약학 전공과 경영학을 같이 하면 뭐가 좋나요?")
    
    st.success("💎 **바이오 + 경영 = 최강 조합!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 바이오산업 특성")
        st.info("""
        **왜 경영이 중요한가?**
        - R&D 비용 막대 (수천억)
        - 제품 출시까지 10년+
        - 전략적 포트폴리오 관리 필수
        - 규제 대응 & 파이낸싱 중요
        """)
    
    with col2:
        st.subheader("🎯 졸업생 성과")
        st.metric("바이오헬스케어 진출", "24.9%", "51명")
        st.warning("""
        **진출 분야**
        - 제약회사 경영기획
        - 바이오 스타트업 CEO
        - 헬스케어 제품 매니저
        - 임상시험 프로젝트 관리
        """)
    
    st.subheader("🔬 관련 연구 & 교육")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **융합 과목**
        - 바이오기술 혁신전략
        - 제약마케팅
        - 바이오기업 가치평가
        """)
    
    with col2:
        st.success("""
        **교수진 연구**
        - 제약바이오 ESG 경영
        - 삼성바이오로직스 사례
        - 바이오기업 회계처리
        """)
    
    with col3:
        st.error("""
        **차별화 포인트**
        - 타 대학 대비 독보적
        - 바이오 이해 + 경영 감각
        - 높은 연봉 & 성장성
        """)

with tabs[7]:
    st.header("🏥 차의과학대 경영학과만의 특별한 점이 있나요?")
    
    st.error("🌟 **바이오헬스케어 특화 경영학!**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏥 차병원 네트워크")
        st.metric("차병원그룹 취업", "10.9%", "24명+")
        st.info("""
        **계열사 진출**
        - 차병원 (분당/강남/일산)
        - 차바이오텍
        - 차메디텍
        - 차케어스
        """)
    
    with col2:
        st.subheader("📚 특화 커리큘럼")
        st.success("""
        **헬스케어 과목**
        - 의료경영
        - 바이오산업론
        - 의료서비스마케팅
        - 헬스케어 데이터분석
        """)
    
    with col3:
        st.subheader("🤝 융합 전공")
        st.warning("""
        **시너지 조합**
        - 디지털보건의료
        - AI의료데이터
        - 바이오식의약학
        - 미디어커뮤니케이션
        """)
    
    st.subheader("🔬 연구 네트워크")
    st.info("""
    **협력 기관**: 한국조세재정연구원 | 국회예산정책처 | 금융감독원 | 건강보험공단
    
    **국제 저널 게재**: Psychology & Marketing | 한국방송학보 | 한국언론학보
    """)

with tabs[8]:
    st.header("🎓 선배들은 주로 어디로 취업하나요?")
    
    # 핵심 지표
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("취업률", "88.7%", "196명")
    with col2:
        st.metric("창업", "5.4%", "12명")
    with col3:
        st.metric("대학원", "5.9%", "13명")
    with col4:
        st.metric("전체 졸업생", "100%", "221명")
    
    # 산업별 & 직무별
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 산업별 분포")
        st.info("""
        1️⃣ **바이오헬스케어** - 24.9%
        2️⃣ **금융** - 19.5%
        3️⃣ **IT** - 19.0%
        4️⃣ **차병원그룹** - 10.9%
        5️⃣ **기타** - 25.7%
        """)
    
    with col2:
        st.subheader("💼 직무별 분포")
        st.warning("""
        1️⃣ **경영기획** - 48.9%
        2️⃣ **회계세무금융** - 20.8%
        3️⃣ **마케팅** - 14.0%
        4️⃣ **기타** - 16.3%
        """)
    
    st.subheader("🌟 주요 취업처")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.success("""
        **금융/증권**
        - 하나은행
        - SK증권
        - 신한은행
        - KB국민은행
        """)
    
    with col2:
        st.info("""
        **대기업**
        - 현대자동차
        - 삼성바이오로직스
        - 롯데
        - CJ올리브영
        """)
    
    with col3:
        st.warning("""
        **IT/플랫폼**
        - 쿠팡
        - 스마일게이트
        - 메가존클라우드
        - 이랜드
        """)
    
    with col4:
        st.error("""
        **병원/헬스케어**
        - 세브란스병원
        - 강남세브란스
        - 차병원 계열
        - 제약회사
        """)

with tabs[9]:
    st.header("🎨 예술 쪽에 관심이 많은데, 경영학 전공이 도움이 될까요?")
    
    st.success("🎭 **문화예술경영 분야로 진출 가능!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 진로 분야")
        st.info("""
        **문화예술 직무**
        - 공연기획자 (PD)
        - 미술관 큐레이터
        - 문화마케터
        - 엔터테인먼트 경영
        - 축제/이벤트 기획
        - 갤러리 운영
        """)
    
    with col2:
        st.subheader("💼 실제 취업 사례")
        st.warning("""
        **졸업생 진출처**
        - FNC엔터테인먼트
        - 환경재단 (서울환경영화제)
        - 광고대행사
        - 방송사
        - 문화재단
        """)
    
    st.subheader("📚 관련 지식 & 연구")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **활용 과목**
        - 소비자행동 분석
        - SNS 마케팅
        - 프로젝트 관리
        - 브랜딩 전략
        """)
    
    with col2:
        st.info("""
        **교수진 연구**
        - 리뷰 효과 분석
        - 도시브랜딩
        - 관광심리학
        - K-콘텐츠 해외진출
        """)
    
    with col3:
        st.error("""
        **왜 필요한가?**
        - 예술도 관객이 있어야 함
        - 수익모델 설계 필수
        - 마케팅 없인 생존 불가
        - 경영 = 예술의 날개
        """)

with tabs[10]:
    st.header("🤖 디지털보건의료 vs AI의료데이터, 뭘 같이 공부하는 게 나을까요?")
    
    st.warning("🎯 **두 분야 모두 매력적이지만 방향이 다릅니다!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏥 디지털보건의료 + 경영")
        st.info("""
        **특징**
        - 헬스케어 비즈니스 분야
        - 서비스 기획 중심
        - 사람과의 소통 중요
        
        **진로**
        - 병원 경영기획
        - 디지털 헬스 서비스 기획
        - 의료기기 마케팅
        - 헬스케어 스타트업
        
        **관련 연구**
        - 의료서비스 품질
        - AI 로봇 수용성
        - 환자 경험 개선
        """)
    
    with col2:
        st.subheader("📊 AI의료데이터 + 경영")
        st.success("""
        **특징**
        - 비즈니스 애널리틱스 분야
        - 데이터 분석 중심
        - 정량적 의사결정
        
        **진로**
        - 헬스케어 데이터 분석가
        - 보험 리스크 분석
        - 임상데이터 관리
        - AI 서비스 기획
        
        **관련 연구**
        - ESG 빅데이터 분석
        - 예측모형 개발
        - 리얼월드데이터 활용
        """)
    
    st.error("""
    💡 **선택 기준**
    - 사람과 소통 좋아함 → 디지털보건의료
    - 데이터 분석 좋아함 → AI의료데이터
    - 둘 다 경영학과 시너지 극대화!
    """)

with tabs[11]:
    st.header("📺 미디어커뮤니케이션이랑 경영학을 같이 하면 어떤가요?")
    
    st.success("🎯 **완벽한 조합! 미디어 경영 전문가로 성장**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💼 진로 분야")
        st.info("""
        **미디어 경영 직무**
        - IR (투자자 관계)
        - PR (홍보)
        - 콘텐츠 비즈니스
        - 브랜드 커뮤니케이션
        - 디지털 마케팅
        - 인플루언서 마케팅
        """)
    
    with col2:
        st.subheader("🌟 시대적 트렌드")
        st.warning("""
        **왜 중요한가?**
        - 모든 기업 = 미디어 기업
        - 유튜브/인스타 자체 채널 운영
        - 스토리텔링 = 핵심 역량
        - 콘텐츠 = 새로운 자산
        """)
    
    st.subheader("📚 관련 연구 & 강점")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **교수진 연구**
        - SNS 마케팅 효과
        - 온라인 리뷰 영향력
        - K-콘텐츠 해외진출
        - 인플루언서 ROI
        """)
    
    with col2:
        st.info("""
        **핵심 역량**
        - 스토리텔링 능력
        - 경영 감각
        - 데이터 분석력
        - 크리에이티브
        """)
    
    with col3:
        st.error("""
        **취업처**
        - 광고대행사
        - 방송사 전략팀
        - 기업 커뮤니케이션실
        - MCN 기업
        """)

with tabs[12]:
    st.header("😰 수학이나 회계를 전혀 모르는데 따라갈 수 있을까요?")
    
    st.success("😊 **걱정 마세요! 기초부터 차근차근 가르칩니다**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 단계별 학습")
        st.info("""
        **1학년 기초 과목**
        - 회계원리: 자산=부채+자본부터
        - 경영통계: 평균, 분산부터
        - 경영학원론: 큰 그림부터
        
        **필요 수학 수준**
        - 고등학교 수준이면 충분
        - 복잡한 미적분 불필요
        - 기본 사칙연산 + α
        """)
    
    with col2:
        st.subheader("🤝 지원 프로그램")
        st.warning("""
        **학습 지원**
        - 교수학습지원센터 튜터링
        - 선배 멘토링 프로그램
        - SPSS/R 수업 내 교육
        - 교수님 오피스아워
        
        **목표**
        - 원칙과 이론 깊은 이해
        - 실무 적용 능력
        - 체계적 사고력
        """)
    
    st.error("""
    💪 **선배의 응원**
    "저도 수포자였는데 지금은 회계사 준비 중이에요! 대부분 학생이 아무것도 모르고 시작해요. 
    교수님들이 정말 친절하게 알려주시고, 기초부터 탄탄히 배울 수 있어요!"
    """)

with tabs[13]:
    st.header("🎬 영상이나 광고를 만드는 걸 좋아하는데, 경영학이랑 어떻게 연결할 수 있을까요?")
    
    st.success("🚀 **영상 제작 + 경영 전략 = 최강 콘텐츠 크리에이터!**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💡 시너지 효과")
        st.info("""
        **창의성 + 전략성**
        - 마케팅 프레임워크 → 영상 기획
        - 타겟 분석 → 콘텐츠 최적화
        - ROI 측정 → 효과 검증
        
        **비즈니스 콘텐츠**
        - 단순 예쁜 영상 ❌
        - 목표 달성하는 콘텐츠 ⭕
        - 데이터 기반 크리에이티브
        """)
    
    with col2:
        st.subheader("🎯 실무 활용")
        st.warning("""
        **기업 실무**
        - A/B 테스트로 영상 최적화
        - 데이터 기반 크리에이티브 개선
        - 인플루언서 마케팅 ROI 분석
        - SNS 캠페인 효과 측정
        
        **차별화 포인트**
        - 창의적 + 분석적
        - 아트 + 사이언스
        - 감성 + 이성
        """)
    
    st.subheader("📚 관련 교육 & 연구")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **활용 과목**
        - 디지털 마케팅
        - 소비자행동 연구
        - 브랜드 전략
        - 콘텐츠 비즈니스
        """)
    
    with col2:
        st.info("""
        **교수진 연구**
        - 인플루언서 마케팅 ROI
        - SNS 캠페인 효과
        - 영상 콘텐츠 최적화
        - 크리에이티브 전략
        """)
    
    with col3:
        st.error("""
        **진로**
        - 광고 기획자
        - 콘텐츠 PD
        - 브랜드 필름 감독
        - 디지털 마케터
        """)

# Footer
st.markdown("---")
st.caption("📧 문의: 미래융합대학 헬스케어융합학부 박대근 교수 | 🌐 전공 홈페이지: biz.cha.ac.kr")





