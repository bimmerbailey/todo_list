FROM node:15
WORKDIR /app

COPY package*.json /app/

#ARG NODE_ENV
#RUN if [ "$NODE_ENV" = "development" ]; \
#        then npm install; \
#        else npm install --only=production; \
#        fi

RUN yarn install

COPY ./ /app/

RUN npm run build
