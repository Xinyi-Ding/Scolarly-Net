FROM node:20 as build-stage

WORKDIR /frontend

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# run the app in a nginx server
FROM nginx:stable as prod-stage

COPY --from=build-stage /frontend/dist/ /usr/share/nginx/html/

#COPY default.conf /etc/nginx/conf.d/default.conf
CMD ["cat", "/etc/nginx/nginx.conf"]

EXPOSE 81

CMD ["nginx", "-g", "daemon off;"]
