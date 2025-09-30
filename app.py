import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="경영학전공 완전정복 가이드",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 경영학전공 완전정복 가이드")
st.caption("미래융합대학 헬스케어융합학부 | 박대근 교수")

# HTML 코드 - 경영학전공 가이드 + D-ID 에이전트
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>교수님들과 함께하는 1문 N답</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
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
        
        .professor-info {
            color: #7f8c8d;
            font-size: 1.1rem;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: #95a5a6;
            font-size: 0.95rem;
        }
        
        .last-updated {
            color: #3498db;
            font-size: 0.9rem;
            margin-top: 10px;
        }
        
        .navigation {
            background: white;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }
        
        .nav-title {
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.1rem;
        }
        
        .nav-links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .nav-link {
            background: #f8f9fa;
            padding: 8px 15px;
            border-radius: 20px;
            color: #667eea;
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            font-family: inherit;
        }
        
        .nav-link:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
        }
        
        .quiz-section {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }
        
        .quiz-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #ecf0f1;
        }
        
        .quiz-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            color: white;
            font-size: 20px;
        }
        
        .quiz-title {
            font-size: 1.3rem;
            color: #2c3e50;
            font-weight: 600;
        }
        
        .quiz-item {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .quiz-item:hover {
            transform: translateX(5px);
            border-color: #667eea;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
        }
        
        .quiz-answer {
            display: none;
            margin-top: 15px;
            padding: 15px;
            background: white;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        .quiz-answer.active {
            display: block;
            animation: slideDown 0.3s ease;
        }
        
        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .section-title {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            margin: 40px 0 20px 0;
            font-size: 1.3rem;
            text-align: center;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }
        
        .qna-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }
        
        .qna-card:hover {
            transform: translateY(-5px);
        }
        
        .question {
            font-size: 1.2rem;
            color: #2c3e50;
            font-weight: 600;
            margin-bottom: 15px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .question-number {
            display: inline-block;
            width: 35px;
            height: 35px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            text-align: center;
            line-height: 35px;
            border-radius: 50%;
            margin-right: 15px;
            font-weight: bold;
            font-size: 0.9rem;
        }
        
        .toggle-icon {
            font-size: 1.5rem;
            transition: transform 0.3s ease;
            color: #667eea;
        }
        
        .answer {
            display: none;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            margin-top: 15px;
            line-height: 1.8;
        }
        
        .answer.active {
            display: block;
            animation: slideDown 0.3s ease;
        }
        
        .answer h3 {
            color: #667eea;
            margin: 20px 0 10px 0;
            font-size: 1.1rem;
        }
        
        .answer ul {
            margin-left: 20px;
            margin-top: 10px;
        }
        
        .answer li {
            margin-bottom: 8px;
        }
        
        .highlight {
            background: linear-gradient(to bottom, transparent 60%, #ffd93d 60%);
            padding: 2px 4px;
            font-weight: 500;
        }
        
        .tag {
            display: inline-block;
            background: #e3f2fd;
            color: #1976d2;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.9rem;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        
        .track-card {
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }
        
        .track-card:hover {
            border-color: #667eea;
            transform: scale(1.02);
        }
        
        .track-title {
            color: #667eea;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        .percentage-bar {
            background: #ecf0f1;
            height: 30px;
            border-radius: 15px;
            margin: 10px 0;
            position: relative;
            overflow: hidden;
        }
        
        .percentage-fill {
            height: 100%;
            border-radius: 15px;
            display: flex;
            align-items: center;
            padding-left: 10px;
            color: white;
            font-weight: 600;
            transition: width 1s ease;
        }
        
        .stat-card {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }
        
        .stat-label {
            color: #7f8c8d;
            font-size: 0.95rem;
        }
        
        .timeline {
            position: relative;
            padding-left: 30px;
            margin: 20px 0;
        }
        
        .timeline::before {
            content: '';
            position: absolute;
            left: 10px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: #667eea;
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 20px;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -25px;
            top: 5px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #667eea;
            border: 2px solid white;
        }
        
        .timeline-date {
            color: #667eea;
            font-weight: 600;
            margin-bottom: 5px;
        }
        
        .timeline-content {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        @media (max-width: 768px) {
            h1 {
                font-size: 1.5rem;
            }
            
            .question {
                font-size: 1rem;
            }
            
            .container {
                padding: 15px;
            }
            
            .nav-links {
                flex-direction: column;
            }
            
            .nav-link {
                width: 100%;
                text-align: center;
            }
        }
        
        .progress-bar {
            background: #ecf0f1;
            height: 8px;
            border-radius: 4px;
            margin: 20px 0;
            overflow: hidden;
            position: sticky;
            top: 10px;
            z-index: 100;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            width: 0%;
            transition: width 0.5s ease;
        }
        
        .completion-message {
            display: none;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin-top: 30px;
            font-size: 1.2rem;
        }
        
        .tip-box {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        
        .info-box {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        
        .warning-box {
            background: #ffebee;
            border-left: 4px solid #f44336;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }
        
        .reference-box {
            background: #f5f5f5;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            font-size: 0.9rem;
        }
        
        /* D-ID Agent Styles */
        #did-agent-container {
            font-size: 12px !important;
        }
        #did-agent-container .agent-video,
        #did-agent-container .agent-avatar,
        #did-agent-container video,
        #did-agent-container img {
            display: block !important;
            margin: 0 auto !important;
            text-align: center !important;
        }
        #did-agent-container .video-container,
        #did-agent-container .avatar-container,
        #did-agent-container .agent-container {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }
        #did-agent-container button {
            font-size: 10px !important;
            padding: 6px 10px !important;
        }
        #did-agent-container button[type="button"],
        #did-agent-container .start-button,
        #did-agent-container .conversation-button {
            font-size: 9px !important;
            text-transform: none !important;
            letter-spacing: normal !important;
        }
        #did-agent-container button span,
        #did-agent-container button div {
            font-size: 9px !important;
        }
        #did-agent-container .message,
        #did-agent-container .chat-text,
        #did-agent-container p {
            font-size: 10px !important;
        }
        #did-agent-container input,
        #did-agent-container textarea {
            font-size: 10px !important;
        }
        #did-agent-container .mic-button,
        #did-agent-container .microphone-button {
            transform: scale(0.8) !important;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎓 경영학전공 완전정복 가이드</h1>
            <p class="professor-info">미래융합대학 헬스케어융합학부 | 박대근 교수</p>
            <p class="subtitle">교육, 연구, 진로 및 융합전공에 대한 모든 궁금증을 해결해드립니다</p>
            <p class="last-updated">📅 최종 업데이트: 2025년 2월 (졸업생 383명 데이터 반영)</p>
        </header>
        
        <!-- 빠른 네비게이션 -->
        <div class="navigation">
            <div class="nav-title">🚀 빠른 이동</div>
            <div class="nav-links">
                <button type="button" class="nav-link" onclick="scrollToSection('section-history')">경영학의 역사</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-research')">연구와 교육</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-tracks')">세부 트랙</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-cha-merit')">차의과학대 강점</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-fusion')">복수전공</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-career')">취업 현황</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-tips')">학습 팁</button>
                <button type="button" class="nav-link" onclick="scrollToSection('section-projects')">프로젝트</button>
            </div>
        </div>
        
        <!-- 예습 퀴즈 섹션 -->
        <div class="quiz-section">
            <div class="quiz-header">
                <div class="quiz-icon">💡</div>
                <div class="quiz-title">시작하기 전, 호기심 체크!</div>
            </div>
            <div class="quiz-item" onclick="toggleQuiz(this)">
                <strong>🤔 경영학은 언제부터 시작되었을까요?</strong>
                <div class="quiz-answer">
                    산업혁명 이후 1900년대 초 테일러의 '과학적 관리법'부터 체계화되기 시작했어요! 이후 호손 연구, 일본의 TPS/카이젠, 최근의 디지털 전환까지 계속 진화하고 있습니다. 🏭➡️💻
                </div>
            </div>
            <div class="quiz-item" onclick="toggleQuiz(this)">
                <strong>📊 우리 졸업생들은 어디로 가장 많이 취업하나요?</strong>
                <div class="quiz-answer">
                    383명 분석 결과: 바이오헬스케어(24.5%), IT(19.2%), 금융(18.8%), 기타(27.9%), 차병원그룹(11.5%)! 정말 다양한 분야로 진출하고 있어요! 💼
                </div>
            </div>
            <div class="quiz-item" onclick="toggleQuiz(this)">
                <strong>🎯 경영학의 대표적인 '발명'은 무엇일까요?</strong>
                <div class="quiz-answer">
                    밸런스드 스코어카드(BSC), 활동기준원가(ABC), 도요타 생산방식(TPS), 린 스타트업 등! 이런 혁신적 관리기법들이 전 세계 기업을 변화시켰어요! 💡
                </div>
            </div>
        </div>
        
        <!-- 진도 표시 -->
        <div class="progress-bar">
            <div class="progress-fill" id="progress"></div>
        </div>
        
        <!-- 섹션 0: 경영학의 역사와 도전기 -->
        <div class="section-title" id="section-history">📚 Special Section: 경영학의 역사와 도전기</div>
        
        <div class="qna-card">
            <div class="question" onclick="toggleAnswer(this)">
                <span style="display: flex; align-items: center;">
                    <span class="question-number">SP</span>
                    경영학은 어떻게 발전해왔나요? 주요 혁신과 '발명'들
                </span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="answer">
                <h3>🏛️ 경영학의 진화 Timeline</h3>
                
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-date">1900-1920s: 과학적 관리의 시대</div>
                        <div class="timeline-content">
                            <strong>프레더릭 테일러의 과학적 관리법</strong><br>
                            • 시간동작연구로 작업 효율 극대화<br>
                            • 표준화된 작업 방식 도입<br>
                            • "최선의 방법(One Best Way)" 추구
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-date">1930-1950s: 인간관계론의 등장</div>
                        <div class="timeline-content">
                            <strong>호손 연구(Hawthorne Studies)</strong><br>
                            • 작업자의 심리적 요인 발견<br>
                            • 조직행동론의 태동<br>
                            • 사회심리적 동기부여 중요성 인식
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-date">1950-1980s: 시스템과 상황이론</div>
                        <div class="timeline-content">
                            <strong>OR/관리과학의 부상</strong><br>
                            • 2차 대전 후 수학적 최적화 도입<br>
                            • 시스템 사고와 상황적합 이론<br>
                            • 컴퓨터 활용한 의사결정 지원
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- 섹션 1: 경영학 연구와 교육 -->
        <div class="section-title" id="section-research">📚 Section 1: 경영학 연구와 교육의 세계</div>
        
        <div class="qna-card">
            <div class="question" onclick="toggleAnswer(this)">
                <span style="display: flex; align-items: center;">
                    <span class="question-number">Q1</span>
                    경영학 분야에서는 어떤 연구를 하나요? 교수님들의 연구 분야는?
                </span>
                <span class="toggle-icon">+</span>
            </div>
            <div class="answer">
                <p>경영학 연구는 매우 다양하고 실용적입니다! 최신 연구 트렌드와 우리 교수님들의 전문 분야를 소개합니다:</p>
                
                <h3>🌱 ESG 경영 연구 (최신 트렌드)</h3>
                <p><span class="highlight">2,000편 이상의 메타분석 결과</span>, ESG 수준이 높은 기업이 재무성과도 우수한 것으로 나타났습니다!</p>
                <ul>
                    <li>환경·사회·지배구조와 기업가치의 관계</li>
                    <li>지속가능경영의 재무적 타당성</li>
                    <li>ESG 투자 의사결정 패턴 분석</li>
                </ul>
            </div>
        </div>
        
        <!-- 추가 섹션들... -->
        
        <!-- 복습 퀴즈 섹션 -->
        <div class="quiz-section">
            <div class="quiz-header">
                <div class="quiz-icon">✓</div>
                <div class="quiz-title">배운 내용 최종 점검!</div>
            </div>
            <div class="quiz-item" onclick="toggleQuiz(this)">
                <strong>📝 Quiz 1: 우리 졸업생 중 바이오헬스케어 취업 비율은?</strong>
                <div class="quiz-answer">
                    <strong>정답: 24.5%</strong><br>
                    차병원그룹(11.5%)을 포함하면 총 36%! 차의과학대의 특성이 잘 나타나는 수치입니다.
                </div>
            </div>
        </div>
        
        <div class="completion-message" id="completionMessage">
            🎉 축하합니다! 경영학전공 완전정복 완료!<br><br>
            이제 여러분은 차의과학대 경영학전공에 대해 완벽히 이해하셨습니다.<br>
            383명의 선배들이 걸어간 길, 여러분도 할 수 있습니다!<br><br>
            "경영학은 모든 조직의 언어이자, 미래를 설계하는 도구입니다."<br><br>
            📧 문의: 미래융합대학 헬스케어융합학부 박대근 교수<br>
            🌐 전공 홈페이지: biz.cha.ac.kr
        </div>
    </div>
    
    <!-- D-ID Agent Container -->
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
        // 스크롤 기능
        function scrollToSection(sectionId) {
            const element = document.getElementById(sectionId);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
        
        // 답변 토글 기능
        function toggleAnswer(element) {
            const answer = element.nextElementSibling;
            const icon = element.querySelector('.toggle-icon');
            
            answer.classList.toggle('active');
            icon.textContent = answer.classList.contains('active') ? '−' : '+';
            icon.style.transform = answer.classList.contains('active') ? 'rotate(180deg)' : 'rotate(0deg)';
            
            updateProgress();
            
            if (answer.classList.contains('active')) {
                setTimeout(() => {
                    element.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            }
        }
        
        // 퀴즈 토글 기능
        function toggleQuiz(element) {
            const answer = element.querySelector('.quiz-answer');
            answer.classList.toggle('active');
            
            const allQuizItems = element.parentElement.querySelectorAll('.quiz-item');
            allQuizItems.forEach(item => {
                if (item !== element) {
                    item.querySelector('.quiz-answer').classList.remove('active');
                }
            });
            
            updateProgress();
        }
        
        // 진도 업데이트
        function updateProgress() {
            const totalItems = document.querySelectorAll('.answer, .quiz-answer').length;
            const activeItems = document.querySelectorAll('.answer.active, .quiz-answer.active').length;
            const percentage = (activeItems / totalItems) * 100;
            
            document.getElementById('progress').style.width = percentage + '%';
            
            if (percentage === 100) {
                document.getElementById('completionMessage').style.display = 'block';
                document.getElementById('completionMessage').style.animation = 'pulse 2s infinite';
            }
        }
        
        // 페이지 로드 시 애니메이션
        window.addEventListener('load', () => {
            const percentageFills = document.querySelectorAll('.percentage-fill');
            setTimeout(() => {
                percentageFills.forEach(fill => {
                    const width = fill.style.width;
                    fill.style.width = '0%';
                    setTimeout(() => {
                        fill.style.width = width;
                    }, 100);
                });
            }, 500);
        });
        
        // 부드러운 스크롤 효과
        document.querySelectorAll('.question').forEach(q => {
            q.addEventListener('click', function() {
                this.style.transform = 'scale(0.98)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 200);
            });
        });
        
        // 펄스 애니메이션 정의
        const style = document.createElement('style');
        style.textContent = `
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        `;
        document.head.appendChild(style);
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
"""

# HTML 컴포넌트 렌더링
components.html(html_code, height=1500, scrolling=True)


















