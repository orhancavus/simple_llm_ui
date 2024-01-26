import streamlit as st
import requests


# Function to initialize session state
def init_session_state():
    if "enter_pressed" not in st.session_state:
        st.session_state.enter_pressed = False


def get_completion(prompt):
    endpoint = "http://127.0.0.1:8080/completion"
    payload = {
        "prompt": prompt,
        "n_predict": 512,
    }
    response = requests.post(endpoint, json=payload)
    return response.json().get("content", "")


def main():
    st.title("Local LLM Chat Application")

    # Initialize session state
    init_session_state()

    # Use a form to capture enter key press
    with st.form("prompt_form"):
        # Accept user input
        user_prompt = st.text_input("Enter your prompt:")

        # Add a submit button inside the form
        submit_button = st.form_submit_button("Submit")

    # Check if the button is clicked or enter key is pressed
    if submit_button or st.session_state.enter_pressed:
        # Reset enter_pressed
        st.session_state.enter_pressed = False

        # Check if the user has entered a prompt
        if user_prompt:
            # Call the endpoint and get the completion
            completion_result = get_completion(user_prompt)

            # Display the result on the same page
            st.subheader("Result:")
            # st.write(completion_result)
            st.code(completion_result)

        else:
            st.warning("Please enter a prompt.")


if __name__ == "__main__":
    main()
