# FastAPI Question Answering Web Application

## Description
This project is a web application built with FastAPI, HTML, CSS, and JavaScript. It allows users to upload a text file of questions, which are then answered using a chat model from the Ollama library.

## Installation
To get this project up and running, follow these steps:

1. Clone this repository: `git clone https://github.com/Aniruddha-kale/MFG-598-Project.git`
2. Install Ollama from : `https://ollama.com/download`
3. Run this command in terminal : `ollama pull llama3`
4. Install the required libraries: `pip install fastapi uvicorn ollama`
5. Run the server: `uvicorn main:app --reload`

## Usage
To use this application, navigate to `localhost:8000` in your web browser. Click 'Choose File' to select a text file of questions, then click 'Submit'. The answers to your questions will be displayed on the page.

## Demo
Watch a demonstration of this project here:
https://drive.google.com/file/d/1TYpSMHTkdt2_JDu73opIpr0K-sDfei_e/view?usp=sharing
