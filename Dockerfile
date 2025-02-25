# Using the official Python image as base
FROM python:3.9

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the entire application
COPY . .

# Exposing the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
