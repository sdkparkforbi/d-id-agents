import streamlit as st
import streamlit.components.v1 as components
import json
import base64

# 페이지 설정
st.set_page_config(
    page_title="D-ID AI Agent with ElevenLabs Voice",
    page_icon="🎭",
    layout="wide"
)

# CSS 스타일
st.markdown("""
<style>
    .main {
        padding: 1rem;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 10px;
        font-weight: 600;
    }
    .info-box {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎭 D-ID AI Agent + ElevenLabs Voice")
st.markdown("---")

# 설정 정보
VOICE_ID = "uyVNoMrnUku1dZyVEXwD"  # 제공하신 ElevenLabs Voice ID
ELEVENLABS_API_KEY = "sk_1686275d9d8da2797a4a2ba784efdcc8bc2436dc21ac9af5"

# 사이드바 설정
with st.sidebar:
    st.header("⚙️ Agent 설정")
    
    st.markdown(f"""
    <div class="info-box">
    <b>🎙️ ElevenLabs Voice</b><br>
    Voice ID: <code>{VOICE_ID}</code><br>
    <a href="https://elevenlabs.io/app/voice-library?voiceId={VOICE_ID}" target="_blank">
    🔗 Voice Library에서 확인
    </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("음성 설정")
    stability = st.slider("Stability", 0.0, 1.0, 0.5, 0.1)
    similarity_boost = st.slider("Similarity Boost", 0.0, 1.0, 0.75, 0.1)
    
    st.subheader("Agent 설정")
    agent_name = st.text_input("Agent 이름", value="AI Assistant")
    initial_message = st.text_area(
        "인사 메시지",
        value="안녕하세요! 무엇을 도와드릴까요?",
        height=100
    )
    
    st.markdown("---")
    st.markdown("""
    ### 📋 사용 방법:
    1. Agent가 로드될 때까지 잠시 기다려주세요
    2. 마이크 버튼을 클릭하여 대화를 시작하세요
    3. 텍스트로도 입력 가능합니다
    
    ### ✨ 특징:
    - 🎙️ ElevenLabs 고품질 음성
    - 💬 실시간 대화형 인터페이스
    - 🎭 자연스러운 립싱크
    - 🔊 음성 인식 지원
    """)

# 메인 컨텐츠
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("💬 AI Agent 채팅")
    
    # Agent 설정을 포함한 HTML 코드
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
            }}
            #did-agent-container {{
                width: 100%;
                height: 700px;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                position: relative;
            }}
            .loading {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: white;
                font-size: 1.5em;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div id="did-agent-container">
            <div class="loading">
                <div>🎭</div>
                <div>Agent 로딩 중...</div>
            </div>
        </div>
        
        <script type="module">
            // D-ID Agent 설정
            const agentConfig = {{
                mode: "full",
                clientKey: "Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll",
                agentId: "v2_agt_Iog7Y5Ky",
                name: "{agent_name}",
                monitor: true,
                targetId: "did-agent-container",
                // ElevenLabs 음성 설정
                voiceProvider: {{
                    type: "elevenlabs",
                    voiceId: "{VOICE_ID}",
                    apiKey: "{ELEVENLABS_API_KEY}",
                    voiceConfig: {{
                        stability: {stability},
                        similarityBoost: {similarity_boost}
                    }}
                }},
                // 초기 메시지
                initialMessage: "{initial_message}",
                // 추가 설정
                language: "ko-KR",
                enableMicrophone: true,
                enableCamera: false,
                chatMode: "text_and_voice"
            }};
            
            // Agent 스크립트 동적 로드
            const script = document.createElement('script');
            script.type = 'module';
            script.src = 'https://agent.d-id.com/v2/index.js';
            
            // data 속성 설정
            Object.keys(agentConfig).forEach(key => {{
                const dataKey = 'data-' + key.replace(/([A-Z])/g, '-$1').toLowerCase();
                if (typeof agentConfig[key] === 'object') {{
                    script.setAttribute(dataKey, JSON.stringify(agentConfig[key]));
                }} else {{
                    script.setAttribute(dataKey, agentConfig[key]);
                }}
            }});
            
            // 스크립트 로드 이벤트
            script.onload = () => {{
                console.log('D-ID Agent loaded successfully');
                // ElevenLabs 음성 설정 적용
                if (window.DIDAgent && window.DIDAgent.setVoiceProvider) {{
                    window.DIDAgent.setVoiceProvider({{
                        type: 'elevenlabs',
                        voiceId: '{VOICE_ID}',
                        apiKey: '{ELEVENLABS_API_KEY}'
                    }});
                }}
            }};
            
            script.onerror = () => {{
                console.error('Failed to load D-ID Agent');
                document.querySelector('.loading').innerHTML = '<div>❌</div><div>Agent 로드 실패</div>';
            }};
            
            document.body.appendChild(script);
            
            // Agent 이벤트 리스너
            window.addEventListener('did-agent-ready', (event) => {{
                console.log('Agent is ready:', event);
                document.querySelector('.loading').style.display = 'none';
            }});
            
            window.addEventListener('did-agent-message', (event) => {{
                console.log('Agent message:', event.detail);
            }});
            
            window.addEventListener('did-agent-error', (event) => {{
                console.error('Agent error:', event.detail);
            }});
        </script>
    </body>
    </html>
    """
    
    # HTML 컴포넌트 렌더링
    components.html(html_code, height=750)

with col2:
    st.subheader("📊 상태")
    
    # 연결 상태 표시
    st.markdown("""
    <div class="info-box">
    <b>🟢 연결 상태</b><br>
    Agent: 활성화<br>
    Voice: ElevenLabs<br>
    Mode: 대화형
    </div>
    """, unsafe_allow_html=True)
    
    # 음성 정보
    st.markdown(f"""
    <div class="info-box">
    <b>🎙️ 음성 정보</b><br>
    Voice ID: <code style="font-size: 0.8em;">{VOICE_ID[:10]}...</code><br>
    Stability: {stability}<br>
    Similarity: {similarity_boost}
    </div>
    """, unsafe_allow_html=True)
    
    # 사용 팁
    st.markdown("""
    ### 💡 사용 팁
    - 🎤 마이크 버튼으로 음성 대화
    - ⌨️ 텍스트 입력도 가능
    - 🔄 새로고침으로 리셋
    """)

# 하단 정보
st.markdown("---")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.metric("Agent 모드", "대화형 챗봇")

with col_b:
    st.metric("음성 제공", "ElevenLabs")

with col_c:
    st.metric("아바타", "D-ID Agent v2")

# 추가 정보
with st.expander("🔧 고급 설정 및 문제 해결"):
    st.markdown("""
    ### 문제 해결:
    - **Agent가 로드되지 않는 경우**: 페이지를 새로고침 해주세요
    - **음성이 나오지 않는 경우**: 브라우저의 오디오 권한을 확인해주세요
    - **마이크가 작동하지 않는 경우**: 브라우저의 마이크 권한을 허용해주세요
    
    ### API 정보:
    - **D-ID Client Key**: 제공된 키 사용 중
    - **ElevenLabs API Key**: 제공된 키 사용 중
    - **Voice ID**: `{}`
    
    ### 지원 브라우저:
    - Chrome (권장)
    - Edge
    - Safari
    - Firefox
    """.format(VOICE_ID))

st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    Made with ❤️ using Streamlit, D-ID Agent & ElevenLabs
</div>
""", unsafe_allow_html=True)
