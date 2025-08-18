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
#       data-target-id="did-agent-container">
# </script>

# """

# components.html(html_code, height=650)


import streamlit as st
import streamlit.components.v1 as components

st.title("D-ID AI Agent")

html_code = """
<div id="did-agent-container" style="width: 100%; height: 600px;"></div>
<script type="module"
      src="https://agent.d-id.com/v2/index.js"
      data-mode="full"
      data-client-key="Z29vZ2xlLW9hdXRoMnwxMTI3NjQ3MzA0NTM3NjA0MTgyMTI6d01EN0x6bFFFMmlZSk9nUHNacXll"
      data-agent-id="v2_agt_Iog7Y5Ky"
      data-name="did-agent"
      data-monitor="true"
      data-target-id="did-agent-container"
      data-auto-emotions="true"
      data-emotion-sensitivity="medium"
      data-personality="expressive"
      data-responsive-expressions="true"
      data-contextual-emotions="true"
      data-natural-expressions="true">
</script>
"""

components.html(html_code, height=650)

