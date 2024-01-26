# Streamlit Prompt Application

## Overview

This is a simple Streamlit application that allows users to input a prompt and submit it to a local runningn LLM endpoint. The application then displays the result from the endpoint on the same page.
The endpoint is a llama.cpp server that is running on localhost.

## Getting Started

1. Make sure you have Python installed on your machine.
2. Install the required libraries by running:

    ```bash
    pip install streamlit requests
    ```

3. Save the provided Python script (e.g., `llm_chat_st_app.py`) on your local machine.

## Running the Application

### Prerequsite

llama.cpp should be installed and running in server mode on localhost <http://0.0.0.0:8080>

<https://github.com/ggerganov/llama.cpp.git>

```bash
./server -c 4096 --host 0.0.0.0 -t 16 --mlock -m ./my_models/TheBloke/LLama2-7B-chat-GGUF/llama-2-7b-chat.Q4_K_M.gguf
```

### Running

Open a terminal and navigate to the directory containing the script. Run the following command to start the Streamlit app:

```bash
streamlit run llm_chat_st_app.py
```

This will launch a local development server, and you can access the application in your web browser.

## Usage

1. Enter a prompt in the text input field.
2. Click the "Submit" button or press "Enter" to send the prompt to the specified endpoint.
3. The result from the endpoint will be displayed on the same page.

Note: The application uses Streamlit's form functionality to capture the "Enter" key press.

## Dependencies

- Streamlit
- Requests

## Author

Orhan Cavus
