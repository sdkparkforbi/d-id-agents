import streamlit as st
import streamlit.components.v1 as components

st.title("")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
/* D-ID 에이전트 컨테이너 내부 스타일 조정 */
#did-agent-container {
    font-size: 12px !important;
}

/* 아바타 이미지/비디오를 중앙 정렬 */
#did-agent-container .agent-video,
#did-agent-container .agent-avatar,
#did-agent-container video,
#did-agent-container img {
    display: block !important;
    margin: 0 auto !important;
    text-align: center !important;
}

/* 아바타 컨테이너 중앙 정렬 */
#did-agent-container .video-container,
#did-agent-container .avatar-container,
#did-agent-container .agent-container {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}

/* Start Conversation 버튼 텍스트 크기 축소 */
#did-agent-container button {
    font-size: 10px !important;
    padding: 6px 10px !important;
}

/* Start Conversation 버튼 특별 처리 */
#did-agent-container button[type="button"],
#did-agent-container .start-button,
#did-agent-container .conversation-button {
    font-size: 9px !important;
    text-transform: none !important;
    letter-spacing: normal !important;
}

/* 모든 버튼 내부 텍스트 */
#did-agent-container button span,
#did-agent-container button div {
    font-size: 9px !important;
}

/* 대화 텍스트 크기 */
#did-agent-container .message,
#did-agent-container .chat-text,
#did-agent-container p {
    font-size: 10px !important;
}

/* 입력 필드 텍스트 크기 */
#did-agent-container input,
#did-agent-container textarea {
    font-size: 10px !important;
}

/* 마이크 버튼 아이콘 크기 조정 */
#did-agent-container .mic-button,
#did-agent-container .microphone-button {
    transform: scale(0.8) !important;
}
</style>
</head>
<body>

<div id="did-agent-container" style="
    width: 240px; 
    height: 340px; 
    position: fixed; 
    bottom: 20px; 
    right: 20px; 
    z-index: 99999; 
    border-radius: 15px; 
    overflow: hidden; 
    box-shadow: 0 10px 30px rgba(0,0,0,0.4); 
    background: white;">
</div>

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

components.html(html_code, height=650)

# import streamlit as st
# import streamlit.components.v1 as components

# st.title("D-ID AI Agent")

# html_code = """
# <div id="did-agent-container" style="width: 80%; height: 600px;"></div>
# <script type="module"
#       src="https://agent.d-id.com/v2/index.js"
#       data-mode="fabio"
#       data-client-key="Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll"
#       data-agent-id="v2_agt_80jV_9EA"
#       data-name="did-agent"
#       data-monitor="true"
#       data-orientation="horizontal"
#       data-position="right"
#       data-target-id="did-agent-container">
# </script>
# """

# components.html(html_code, height=650)
 
# import streamlit as st
# import streamlit.components.v1 as components

# st.title("D-ID AI Agent")

# html_code = """
# <div id="did-agent-container" style="width: 100%; height: 600px;"></div>
# <script type="module"
#       src="https://agent.d-id.com/v2/index.js"
#       data-mode="full"
#       data-client-key="Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll"
#       data-agent-id="v2_agt_Iog7Y5Ky"
#       data-name="did-agent"
#       data-monitor="true"
#       data-target-id="did-agent-container"
#       data-auto-emotions="true"
#       data-emotion-sensitivity="medium"
#       data-personality="expressive"
#       data-responsive-expressions="true"
#       data-contextual-emotions="true"
#       data-natural-expressions="true">
# </script>
# """

# components.html(html_code, height=650)

# import streamlit as st
# import streamlit.components.v1 as components

# st.title("D-ID AI Agent")

# html_code = """
# <div id="did-agent-container" style="width: 100%; height: 600px;"></div>
# <script type="module"
#       src="https://agent.d-id.com/v2/index.js"
#       data-mode="full"
#       data-client-key="Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll"
#       data-agent-id="v2_agt_Iog7Y5Ky"
#       data-name="did-agent"
#       data-monitor="true"
#       data-target-id="did-agent-container"
#       data-auto-emotions="false"
#       data-expression="sad"
#       data-emotion-intensity="0.7">
# </script>
# """

# components.html(html_code, height=650)

# neutral - 중립적인 표정
# surprised - 놀라는 표정
# happy - 기쁜 표정
# sad - 슬픈 표정



















