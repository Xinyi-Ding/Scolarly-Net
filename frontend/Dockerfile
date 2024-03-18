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
CMD ["ls", "/etc/nginx/conf.d"]
CMD ["cat", "/etc/nginx/conf.d/default.conf"]
CMD ["lsof", "-i:80"]
CMD ["lsof", "-i:8000"]

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
