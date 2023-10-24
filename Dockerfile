# Use the official Python image as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app


# Copy your Streamlit Python script to the Docker container
COPY . .

# Install necessary dependencies
RUN pip install -r requirements.txt


# Expose the port that Streamlit runs on
EXPOSE 8501
# Run your Streamlit app
CMD ["streamlit", "run", "phone_number_check.py"]
