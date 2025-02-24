FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENV STREAMLIT_SERVER_HEADLESS true
ENV STREAMLIT_SERVER_PORT 8501
# Run Streamlit when the container starts
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]