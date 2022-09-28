# Base image
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set working directory
WORKDIR /app

# add app
COPY ./apiProject ./

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 3001