### DOCKER COMMAND
https://docs.docker.com/reference/dockerfile/

FROM ubuntu:18.04
COPY ./app



FROM ubuntu:latest (базовый образ)
RUN apt-get update 
COPY ./app


FROM scratch (образ с нуля)




FROM python:3.7.2-alpine3.8 (образ)
LABEL maintainer="jeffmshale@gmail.com" (помогает установить метки (метаданные). Кто делал и т.в.)
ENV ADMIN="jeff" (устанавливает переменные окружение)
RUN apk update && apk upgrade && apk add bash (команды. В данном случае обновление)
COPY . ./app (копирование в конкретную папку)
ADD https://raw.githubusercontent.com/discdiver/pachy-vid/master/sample_vids/vid1.mp4 \
/my_app_directory (скачивание видео)
RUN ["mkdir", "/a_directory"] (создает директории )
CMD ["python", "./my_script.py"] (собственно сам запуск)



docker run -p 5001:5000 simple-python:v1