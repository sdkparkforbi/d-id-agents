import streamlit as st
import streamlit.components.v1 as components

st.title("")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
/* D-ID 에이전트 컨테이너 내부 텍스트 크기 조절 */
#did-agent-container {
    font-size: 12px !important; /* 기본 글자 크기 설정 */
}

/* D-ID 에이전트 내부의 모든 텍스트 요소에 적용 */
#did-agent-container * {
    font-size: inherit !important;
}

/* 버튼 텍스트 크기 조절 */
#did-agent-container button {
    font-size: 11px !important;
}

/* 제목이나 헤더 텍스트 크기 조절 */
#did-agent-container h1, 
#did-agent-container h2, 
#did-agent-container h3 {
    font-size: 13px !important;
}

/* 대화 텍스트 크기 조절 */
#did-agent-container .message,
#did-agent-container .chat-text {
    font-size: 11px !important;
}
</style>
</head>
<body>

<div id="did-agent-container" style="width: 200px; height: 280px; position: fixed; bottom: 20px; right: 20px; z-index: 99999; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.4); background: white;"></div>

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














