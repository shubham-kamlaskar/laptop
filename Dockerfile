FROM python:3.10-slim-buster
COPY . /app
WORKDIR /app
EXPOSE 5000
ENV NAME World
RUN pip install flask numpy pandas scikit-learn
CMD ["python","laptop.py"]