# FastAPI Project Setup

This repository contains a simple guide to help you set up a FastAPI project, create a virtual environment, and install dependencies using pip.

## Getting Started

Follow these steps to set up your FastAPI project:

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
2. Create a virtual environment named venv:
  python -m venv venv
  venv\Scripts\activate

3. You can install dependencies using pip and the provided requirements.txt file:
  pip install -r requirements.txt

4. Running the FastAPI Application
  uvicorn main:app --reload
