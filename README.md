# Movie_Script_Gen


## Overview

The **Movie Script Generator** is a Python-based application that uses OpenAI's GPT-3.5-turbo language model to create dynamic and imaginative movie scripts. The application generates creative scripts complete with dialogues, settings, and character interactions by providing inputs like scenario topic, character names, locations, and emotions.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**
- **OpenAI Python library**  
  Install it using:

  ```bash
  pip install openai
  
- **dotenv Python library**
```bash
     pip install python-dotenv
```
- **Setup**
Clone the repository:

```bash
     git clone <repository_url>
```

- **Create a .env file in the root directory of the project, and add your OpenAI API key:**

```env
Copy code
TEST_OPENAI_API_KEY=<your_api_key>
```
- **Install dependencies:**

```bash
Copy code
pip install -r requirements.txt
```
- **Usage**
Run the movie script generator:

```bash
python test_case.py
```

### Follow the prompts:

- Enter the scenario topic (e.g., action, comedy, thriller, etc.)
- Provide character names
- Provide location names
- Define the emotions for the characters
### The application will generate a movie script based on your input, complete with dialogues, locations, and emotions.
