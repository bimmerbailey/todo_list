FROM node:14
WORKDIR /app

COPY package*.json .

EXPOSE 8080

ARG NODE_ENV
RUN if [ "$NODE_ENV" = "development" ]; \
        then yarn install; \
        else yarn install --only=production; \
        fi

COPY . .

RUN yarn run build
