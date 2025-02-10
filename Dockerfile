FROM python
WORKDIR /app
COPY script.py .
RUN pip install requests
CMD ["python", "script.py"]