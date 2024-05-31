# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

RUN pip install langchain streamlit python-dotenv 
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]