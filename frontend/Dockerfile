# Base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /app

# add app
COPY ./reactProject ./

# install dependencies
RUN npm install

# expose port
EXPOSE 3000