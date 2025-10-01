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

# HTML 코드 (경영학 가이드 + D-ID 에이전트)
html_content = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            padding-right: 280px;
        }
        
        header {
            background: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }
        
        h1 {
            color: #2c3e50;
            font-size: 2rem;
            margin-bottom: 10px;
        }
        
        .navigation {
            background: white;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }
        
        .nav-link {
            background: #f8f9fa;
            padding: 8px 15px;
            border-radius: 20px;
            color: #667eea;
            font-size: 0.9rem;
            border: none;
            cursor: pointer;
            margin: 5px;
        }
        
        .nav-link:hover {
            background: #667eea;
            color: white;
        }
        
        .qna-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }
        
        .question {
            font-size: 1.2rem;
            color: #2c3e50;
            font-weight: 600;
            margin-bottom: 15px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
        }
        
        .answer {
            display: none;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            margin-top: 15px;
        }
        
        .answer.active {
            display: block;
        }
        
        .section-title {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            margin: 40px 0 20px 0;
            font-size: 1.3rem;
            text-align: center;
        }
        
        /* D-ID 에이전트 스타일 */
        #did-agent-container {
            font-size: 12px !important;
        }
        #did-agent-container button {
            font-size: 10px !important;
            padding: 6px 10px !important;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎓 경영학전공 완전정복 가이드</h1>
            <p>미래융합대학 헬스케어융합학부 | 박대근 교수</p>
            <p>교육, 연구, 진로 및 융합전공에 대한 모든 궁금증을 해결해드립니다</p>
            <p>📅 최종 업데이트: 2025년 2월 (졸업생 383명 데이터 반영)</p>
        </header>
        
        <div class="navigation">
            <strong>🚀 빠른 이동</strong><br><br>
            <button class="nav-link" onclick="document.getElementById('section-history').scrollIntoView()">경영학의 역사</button>
            <button class="nav-link" onclick="document.getElementById('section-research').scrollIntoView()">연구와 교육</button>
            <button class="nav-link" onclick="document.getElementById('section-tracks').scrollIntoView()">세부 트랙</button>
            <button class="nav-link" onclick="document.getElementById('section-career').scrollIntoView()">취업 현황</button>
        </div>
        
        <div class="section-title" id="section-history">📚 경영학의 역사와 발전</div>
        
        <div class="qna-card">
            <div class="question" onclick="toggleAnswer(this)">
                <span>경영학은 어떻게 발전해왔나요?</span>
                <span>+</span>
            </div>
            <div class="answer">
                <h3>경영학의 진화 Timeline</h3>
                <p><strong>1900-1920s:</strong> 테일러의 과학적 관리법</p>
                <p><strong>1930-1950s:</strong> 호손 연구와 인간관계론</p>
                <p><strong>1980-2000s:</strong> TPS/카이젠의 글로벌 확산</p>
                <p><strong>2000s-현재:</strong> Industry 4.0과 AI 경영</p>
            </div>
        </div>
        
        <div class="section-title" id="section-research">📚 경영학 연구와 교육</div>
        
        <div class="qna-card">
            <div class="question" onclick="toggleAnswer(this)">
                <span>경영학 분야의 최신 연구 트렌드는?</span>
                <span>+</span>
            </div>
            <div class="answer">
                <h3>🌱 ESG 경영 연구</h3>
                <p>2,000편 이상의 메타분석 결과, ESG 수준이 높은 기업이 재무성과도 우수!</p>
                <h3>🚀 디지털 전환과 비즈니스 모델 혁신</h3>
                <p>AI와 빅데이터 기반 의사결정, 플랫폼 비즈니스 등</p>
            </div>
        </div>
        
        <div class="section-title" id="section-tracks">🎯 경영학의 5개 세부 트랙</div>
        
        <div class="qna-card">
            <div class="question" onclick="toggleAnswer(this)">
                <span>경영학 전공의 5개 세부 트랙은?</span>
                <span>+</span>
            </div>
            <div class="answer">
                <h3>1️⃣ 경영기획 트랙</h3>
                <p>대기업 경영기획실, 전략컨설팅, 사업개발</p>
                
                <h3>2️⃣ 마케팅 트랙</h3>
                <p>브랜드 매니저, 마케팅 AE, 디지털 마케터</p>
                
                <h3>3️⃣ 회계·재무 트랙</h3>
                <p>회계법인, 금융기관, CPA</p>
                
                <h3>4️⃣ 헬스케어 비즈니스 트랙 ✨차의과학대 특화!</h3>
                <p>제약/바이오, 병원경영, 디지털헬스</p>
                
                <h3>5️⃣ 비즈니스 애널리틱스 트랙</h3>
                <p>데이터 분석가, BI 전문가</p>
            </div>
        </div>
        
        <div class="section-title" id="section-career">💼 실제 취업 현황 (383명 분석)</div>
        
        <div class="qna-card">
            <div class="question" onclick="toggleAnswer(this)">
                <span>선배들은 실제로 어디로 취업했나요?</span>
                <span>+</span>
            </div>
            <div class="answer">
                <h3>📊 졸업생 383명 중 208명 취업 현황</h3>
                <p>✅ 바이오·헬스케어 24.5% (51명)</p>
                <p>✅ IT 19.2% (40명)</p>
                <p>✅ 금융 18.8% (39명)</p>
                <p>✅ 차병원그룹 11.5% (24명)</p>
                <p>✅ 기타 27.9% (58명)</p>
                
                <h3>🏢 주요 취업처</h3>
                <p><strong>제약·바이오:</strong> 유한양행, 보령, 녹십자, CMG제약</p>
                <p><strong>병원:</strong> 세브란스, 차병원(분당, 강남, 일산)</p>
                <p><strong>IT:</strong> 메가존클라우드, 쿠팡, 로카모빌리티</p>
            </div>
        </div>
    </div>
    
    <!-- D-ID Agent Container (Fixed) -->
    <div id="did-agent-container" style="
        width: 250px; 
        height: 350px; 
        position: fixed; 
        bottom: 20px; 
        right: 20px; 
        z-index: 99999; 
        border-radius: 15px; 
        overflow: hidden; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.4); 
        background: white;">
    </div>
    
    <script>
        function toggleAnswer(element) {
            const answer = element.nextElementSibling;
            const icon = element.querySelector('span:last-child');
            
            answer.classList.toggle('active');
            icon.textContent = answer.classList.contains('active') ? '−' : '+';
        }
    </script>
    
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
'''

# HTML 렌더링
components.html(html_content, height=1200, scrolling=True)



















