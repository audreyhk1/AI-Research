import streamlit as st

# constants
QUESTION = "Compute the integral of f(x) = x^2."

# Initialize session state
if "help_clicks" not in st.session_state:
    st.session_state.help_clicks = 0
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = None

st.set_page_config(page_title="Interactive Help Interface", layout="centered")

st.markdown("## Sample Question Interface")
st.markdown("")
st.markdown(
    f"<p style='font-size:20px;'>{QUESTION}</p>",
    unsafe_allow_html=True
)
# Outer container for neat padding
with st.container():
    # Question area
    st.text_area(
        label="Type your response here.",
        value="",
        height=100,
        key="question_input",
    )

    st.markdown("")

    # Help Button Logic
    def toggle_help():
        st.session_state.help_clicks += 1
        st.session_state.button_clicked = None  # Reset help text on new toggle

    # Help Button (main toggle)
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.button("Help", on_click=toggle_help)

    # Show 3 sub-buttons if Help clicked an odd number of times
    if st.session_state.help_clicks % 2 == 1:
        st.markdown("### Need Help?")
        st.markdown("Choose an option below to better understand the question.")
        with st.container():
            st.markdown("---")  # Divider for clarity
            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("📝 Explain the question"):
                    st.session_state.button_clicked = "Explain the question"
            with col2:
                if st.button("💡 Give an example"):
                    st.session_state.button_clicked = "Give an example"
            with col3:
                if st.button("🤔 Who cares?"):
                    st.session_state.button_clicked = "Who cares?"

            st.markdown("---")

        # Display response text if a sub-button is clicked
        if st.session_state.button_clicked:
            with st.container():
                st.info(f"**hello world  \n{QUESTION}  \n{st.session_state.button_clicked}**")

# Optional: Add footer or spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# css
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 200px !important;
        height: 3em;
        font-size: 1.1rem;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)