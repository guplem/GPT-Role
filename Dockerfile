FROM python:3.10-slim

WORKDIR /app

RUN pip install langchain streamlit python-dotenv openai
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8501