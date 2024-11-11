# Course-focused Chatbot

A chatbot application built with **Streamlit** and **OpenAI's API** to help students with questions related to any course whose relevant information attached into the project. The chatbot provides responses specifically tailored to the course content, leveraging an intelligent relevance-checking mechanism.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Locally run](#locally_run)

## Overview

This chatbot application uses OpenAI's language models to answer student questions related to an example (Artificial Intelligence and Machine Learning) course. The bot is programmed to respond only to questions relevant to the course content, which is provided through a `.txt` file (`class_info.txt`). The application is designed using Streamlit, offering an interactive and easy-to-use web interface.

## Features

- **Course-Specific Assistance**: The bot only responds to course-relevant questions, ensuring focus.
- **Flexible Content Loading**: Course information is loaded from a `.txt` file, making updates easy.
- **Streamlit Interface**: Provides a user-friendly chat interface.
- **Keyword Filtering**: The chatbot checks for course-related keywords to keep responses on-topic.

## Setup

To get started, follow these steps:

### Prerequisites

- Python 3.7+
- OpenAI API Key (required to access OpenAI's language model)
- Streamlit

## Locally run

   ```bash
   pip install -r requirements.txt
   streamlit run chatbot.py
   ```
