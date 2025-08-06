import streamlit as st
import streamlit.components.v1 as components

st.title("D-ID AI Agent")

# ElevenLabs Voice ID와 API Key
VOICE_ID = "uyVNoMrnUku1dZyVEXwD"
ELEVENLABS_API_KEY = "sk_1686275d9d8da2797a4a2ba784efdcc8bc2436dc21ac9af5"

html_code = f"""
<div id="did-agent-container" style="width: 100%; height: 600px;"></div>
<script type="module">
    import {{ createAgent }} from 'https://agent.d-id.com/v2/index.js';
    
    createAgent({{
        mode: 'full',
        clientKey: 'Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll',
        agentId: 'v2_agt_Iog7Y5Ky',
        name: 'did-agent',
        monitor: true,
        targetId: 'did-agent-container',
        voiceProvider: {{
            type: 'elevenlabs',
            voice_id: '{VOICE_ID}',
            api_key: '{ELEVENLABS_API_KEY}'
        }}
    }});
</script>
"""

components.html(html_code, height=650)
