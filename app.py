import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="경영학전공 완전정복 가이드",
    page_icon="🎓",
    layout="wide"
)

# 제목
st.title("🎓 경영학전공 완전정복 가이드")
st.caption("미래융합대학 헬스케어융합학부 | 박대근 교수")

# 2개 컬럼으로 레이아웃 구성 (7:3 비율)
main_col, agent_col = st.columns([7, 3])

# 메인 컨텐츠 영역
with main_col:
    # 탭 구성
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 경영학 역사", "🎯 세부 트랙", "💼 취업 현황", "🎓 복수전공", "💡 학습 팁"])
    
    with tab1:
        st.header("경영학의 역사와 발전")
        
        with st.expander("🤔 경영학은 언제부터 시작되었을까요?"):
            st.write("""
            산업혁명 이후 1900년대 초 테일러의 '과학적 관리법'부터 체계화되기 시작했어요! 
            이후 호손 연구, 일본의 TPS/카이젠, 최근의 디지털 전환까지 계속 진화하고 있습니다. 🏭➡️💻
            """)
        
        st.subheader("🏛️ 경영학의 진화 Timeline")
        
        st.info("""
        **1900-1920s: 과학적 관리의 시대**
        - 프레더릭 테일러의 과학적 관리법
        - 시간동작연구로 작업 효율 극대화
        - 표준화된 작업 방식 도입
        """)
        
        st.success("""
        **1930-1950s: 인간관계론의 등장**
        - 호손 연구(Hawthorne Studies)
        - 작업자의 심리적 요인 발견
        - 조직행동론의 태동
        """)
        
        st.warning("""
        **1950-1980s: 시스템과 상황이론**
        - 2차 대전 후 수학적 최적화 도입
        - 시스템 사고와 상황적합 이론
        - 컴퓨터 활용한 의사결정 지원
        """)
        
        st.error("""
        **2000s-현재: 디지털 전환 시대**
        - Industry 4.0과 AI 경영
        - 빅데이터와 AI 기반 의사결정
        - 플랫폼 비즈니스 모델
        - ESG 경영과 지속가능성
        """)
    
    with tab2:
        st.header("경영학의 5개 세부 트랙")
        
        track = st.selectbox(
            "관심있는 트랙을 선택하세요:",
            ["경영기획 트랙", "마케팅 트랙", "회계·재무 트랙", "헬스케어 비즈니스 트랙", "비즈니스 애널리틱스 트랙"]
        )
        
        if track == "경영기획 트랙":
            st.write("### 1️⃣ 경영기획 트랙")
            st.write("**핵심 역량:** 경영학 기초, 트렌드 분석, 전략 수립")
            st.write("**주요 과목:** 경영전략, 사업계획서 작성, 조직행동론")
            st.write("**진출 분야:** 대기업 경영기획실, 전략컨설팅, 사업개발")
            st.metric(label="졸업생 진출", value="102명", delta="26.6%")
        
        elif track == "마케팅 트랙":
            st.write("### 2️⃣ 마케팅 트랙")
            st.write("**핵심 역량:** 소비자 분석, 글로벌 시장 대응")
            st.write("**주요 과목:** 마케팅원론, 소비자행동, 디지털마케팅")
            st.write("**진출 분야:** 브랜드 매니저, 마케팅 AE, 디지털 마케터")
            st.metric(label="졸업생 진출", value="30명", delta="7.8%")
        
        elif track == "회계·재무 트랙":
            st.write("### 3️⃣ 회계·재무 트랙")
            st.write("**핵심 역량:** 재무제표 분석, 세무실무, 금융투자")
            st.write("**주요 과목:** 회계원리, 재무관리, 세무회계")
            st.write("**진출 분야:** 회계법인, 금융기관, CPA")
            st.metric(label="졸업생 진출", value="42명", delta="11.0%")
        
        elif track == "헬스케어 비즈니스 트랙":
            st.write("### 4️⃣ 헬스케어 비즈니스 트랙 ✨")
            st.success("차의과학대 특화 트랙!")
            st.write("**핵심 역량:** 헬스케어 산업 융합연구, 파이낸싱, 시장분석")
            st.write("**주요 과목:** 헬스케어경영, 바이오비즈니스, 의료마케팅")
            st.write("**진출 분야:** 제약/바이오, 병원경영, 디지털헬스")
            st.metric(label="바이오헬스케어 취업률", value="24.5%", delta="차병원그룹 11.5% 추가")
        
        else:
            st.write("### 5️⃣ 비즈니스 애널리틱스 트랙")
            st.write("**핵심 역량:** 데이터 기반 시장분석, 모델링")
            st.write("**주요 과목:** 빅데이터분석, 비즈니스애널리틱스")
            st.write("**진출 분야:** 데이터 분석가, BI 전문가")
    
    with tab3:
        st.header("📊 졸업생 383명 취업 현황 분석")
        
        st.subheader("산업별 분포")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("바이오·헬스케어", "24.5%", "51명")
            st.metric("IT", "19.2%", "40명")
            st.metric("금융", "18.8%", "39명")
        
        with col2:
            st.metric("차병원그룹", "11.5%", "24명")
            st.metric("기타", "27.9%", "58명")
        
        st.subheader("주요 취업처")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("""
            **제약·바이오**
            - 유한양행
            - 보령
            - 녹십자
            - 대원제약
            - CMG제약
            - 차바이오텍
            """)
        
        with col2:
            st.success("""
            **병원/의료기관**
            - 세브란스병원
            - 차병원(분당)
            - 차병원(강남)
            - 차병원(일산)
            """)
        
        with col3:
            st.warning("""
            **IT/디지털**
            - 메가존클라우드
            - 쿠팡
            - 로카모빌리티
            - SK증권
            """)
    
    with tab4:
        st.header("🎓 추천 복수전공 조합")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.write("### 💪 경영학 + 스포츠의학")
                st.write("""
                - 스포츠마케팅
                - 스포츠 구단 경영  
                - 퍼포먼스 데이터 분석
                - 헬스케어 서비스 운영
                """)
            
            with st.container():
                st.write("### 🧬 경영학 + 바이오식의약학")
                st.write("""
                - 바이오 비즈니스
                - 제약 마케팅
                - 기업가치평가
                - R&D-사업개발 연결
                """)
        
        with col2:
            with st.container():
                st.write("### 🏥 경영학 + 디지털보건의료")
                st.write("""
                - 병원 운영/경영기획
                - 의료기기·제약 사업개발
                - 디지털헬스 제품 PM
                - 글로벌 헬스케어 전문가
                """)
            
            with st.container():
                st.write("### 🤖 경영학 + AI의료데이터학")
                st.write("""
                - 헬스케어 데이터 애널리스트
                - 보험·결제 데이터 기획
                - 리얼월드데이터 분석
                - 의료 AI 서비스 기획
                """)
    
    with tab5:
        st.header("📚 학습 팁과 조언")
        
        with st.expander("❓ 회계·통계가 약한데 수업을 따라갈 수 있을까요?"):
            st.write("""
            **걱정하지 마세요! 비전공자도 이해할 수 있도록 체계적으로 설계되어 있습니다.**
            
            📚 **단계별 학습 지원:**
            - 회계원리: 비전공자도 이해 가능한 기초부터
            - 경영학원론: 큰 그림부터 차근차근
            - 경영통계: 기초 통계부터 단계적 학습
            
            🤝 **학습 지원 프로그램:**
            - 특강: 빅데이터·통계 기초 특강
            - 튜터링: 선배들의 1:1 학습 지원
            - 학습공동체: 스터디 그룹 운영
            - 오피스아워: 교수님 개별 상담
            """)
        
        st.success("""
        💚 **선배의 한마디:**
        "저도 문과 출신인데 지금은 회계사 준비 중이에요! 학교 커리큘럼 잘 따라가면 충분합니다."
        """)
        
        st.info("""
        🌟 **경영학 전공의 가치**
        - ✅ 모든 조직에는 경영이 필요합니다
        - ✅ 어떤 산업으로든 진출 가능합니다
        - ✅ 창업의 기초 체력을 제공합니다
        - ✅ 글로벌 공통 언어입니다
        - ✅ 평생 활용 가능한 지식입니다
        """)

# 오른쪽 AI 어시스턴트 영역
with agent_col:
    # AI 어시스턴트 컨테이너
    st.markdown("### 🤖 AI 어시스턴트")
    st.caption("궁금한 점을 물어보세요!")
    
    # D-ID 에이전트 HTML
    did_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html, body { 
            margin: 0; 
            padding: 0; 
            width: 100%;
            height: 100%;
            background: white;
            overflow: hidden;
        }
        #did-agent-container {
            width: 50%;
            height: 50%;
            min-height: 300px;
            font-size: 11px !important;
            display: block;
        }
        #did-agent-container button {
            font-size: 9px !important;
            padding: 5px 8px !important;
        }
        #did-agent-container input,
        #did-agent-container textarea {
            font-size: 10px !important;
        }
        /* 에이전트가 로드될 때까지 로딩 메시지 표시 */
        #did-agent-container:empty::before {
            content: "AI 어시스턴트 로딩중...";
            display: block;
            text-align: center;
            padding: 20px;
            color: #666;
        }
    </style>
    </head>
    <body>
    <div id="did-agent-container"></div>
    <script type="module"
          src="https://agent.d-id.com/v2/index.js"
          data-mode="full"
          data-client-key="Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll"
          data-agent-id="v2_agt_80jV_9EA"
          data-name="did-agent"
          data-monitor="true"
          data-target-id="did-agent-container">
    </script>
    </body>
    </html>
    """
    
    # AI 어시스턴트 렌더링 (높이 증가)
    components.html(did_html, height=400, scrolling=False)
    
    # 추가 정보는 제거하여 공간 확보

# Footer
st.markdown("---")
st.caption("📧 문의: 미래융합대학 헬스케어융합학부 박대근 교수 | 🌐 전공 홈페이지: biz.cha.ac.kr")



