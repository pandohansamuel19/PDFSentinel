import streamlit as st


# st.set_page_config(
#     page_title="tf_transformers_malicious_pdf",
#     page_icon="💻",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )


def show() -> None:
    st.markdown("## Your PDF Stats")
    # *! This
    # for this moment give the ui if pdf are benign or malicious
    with st.expander("Click Here for More"):
        number, graph = st.tabs(["Number", "Graph"])

        with number:
            st.markdown(
                "#### This is number's data that generated based on Detection and Analytics from your PDF file")

        with graph:
            st.markdown("#### This is some graph reporting from your PDF file")
