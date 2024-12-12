import streamlit as st
st.set_page_config (layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=800)

with col2:
    st.title("Len: Moments to Memories")
    content = """
    ### Moments to Memories

"Moments to Memories" is a captivating YouTube channel where fleeting moments are transformed into cherished treasures. Through the lens of both the eye and the camera, this channel captures and preserves experiences, turning them into lasting memories. Whether it's a place visited or an event attended, these moments are shared and celebrated, ensuring they remain in our hearts and digital archives for years to come.
    """
    st.info(content)
