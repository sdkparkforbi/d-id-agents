import streamlit as st
import streamlit.components.v1 as components

st.title("D-ID AI Agent")

# ElevenLabs Voice 설정
VOICE_ID = "uyVNoMrnUku1dZyVEXwD"
ELEVENLABS_API_KEY = "sk_1686275d9d8da2797a4a2ba784efdcc8bc2436dc21ac9af5"

html_code = f"""
<div id="did-agent-container" style="width: 100%; height: 600px;"></div>
<script type="module"
      src="https://agent.d-id.com/v2/index.js"
      data-mode="full"
      data-client-key="Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll"
      data-agent-id="v2_agt_Iog7Y5Ky"
      data-name="did-agent"
      data-monitor="true"
      data-target-id="did-agent-container"
      data-elevenlabs-voice-id="{VOICE_ID}"
      data-elevenlabs-api-key="{ELEVENLABS_API_KEY}">
</script>

<script>
    // Agent가 로드된 후 ElevenLabs 설정 적용
    window.addEventListener('did-agent-ready', function(event) {{
        console.log('D-ID Agent is ready');
        
        // Agent 객체에 접근 시도
        if (window.didAgent || window.DIDAgent) {{
            const agent = window.didAgent || window.DIDAgent;
            
            // ElevenLabs 음성 설정 시도
            if (agent.setVoice) {{
                agent.setVoice({{
                    provider: 'elevenlabs',
                    voiceId: '{VOICE_ID}'
                }});
            }}
        }}
    }});
</script>
"""

components.html(html_code, height=650)
