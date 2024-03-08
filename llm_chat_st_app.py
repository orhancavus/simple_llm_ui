import streamlit as st
import requests


def main():
    st.title("Local LLM Chat Application")

    # Initialize session state
    if "enter_pressed" not in st.session_state:
        st.session_state.enter_pressed = False

    # API configurations
    endpoint = "http://127.0.0.1:8080/completion"
    n_predict = 512

    # Use a form to capture enter key press
    with st.form("prompt_form"):
        # Accept user input
        user_prompt = st.text_area("Enter your prompt:")

        # Add a submit button inside the form
        submit_button = st.form_submit_button("Submit")

    # Check if the button is clicked or enter key is pressed
    if submit_button or st.session_state.enter_pressed:
        # Reset enter_pressed
        st.session_state.enter_pressed = False

        # Check if the user has entered a prompt
        if user_prompt:
            # Call the endpoint and get the completion
            payload = {
                "prompt": user_prompt,
                "n_predict": n_predict,
            }
            response = requests.post(endpoint, json=payload)
            completion_result = response.json().get("content", "")

            # Display the result on the same page
            st.subheader("Result:")
            st.code(completion_result)

        else:
            st.warning("Please enter a prompt.")


if __name__ == "__main__":
    main()
