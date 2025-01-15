# Movie Script Generator

## Overview

The Movie Script Generator is a Python application that utilizes the OpenAI GPT-3.5-turbo language model to create imaginative and dynamic movie scripts based on user input. The generated scripts include characters, locations, and emotions, providing a foundation for creative storytelling.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- OpenAI Python library (install using `pip install openai`)
- dotenv Python library (install using `pip install python-dotenv`)

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   

Create a .env file in the project root and add your OpenAI API key:
`TEST_OPENAI_API_KEY=<your_api_key>`

**Usage**

Run the movie script generator:
bash
Copy code
`python test_case.py`
Follow the prompts:
Enter the scenario topic, character names, location names, and emotions as prompted.
Generate a script:
The application will create a movie script based on your input, featuring characters, locations, and emotions.

**Configuration**

Adjust the determine_emotion function in the test_case.py file to customize emotion determination based on dialogue.

