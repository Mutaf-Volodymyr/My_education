## docker build -t myapp:multistage -f Dockerfile.multistage . 


docker build - собирает образ
-t myapp:multistage - название образа : тег
-f Dockerfile.multistage - уточнение имени докер-файла, если название по умолчанию изменено
. - работа в текущей папке

## docker build -t myapp:singlestage -f Dockerfile.singlestage .

## docker images myapp:multistage docker images myapp:singlestage

## docker run -d --name multistage_app -p 5000:5000 myapp:multistage docker run -d --name singlestage_app -p 5001:5001 myapp:singlestage