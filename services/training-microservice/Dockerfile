FROM python:3.10
WORKDIR /app
COPY packages packages
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
