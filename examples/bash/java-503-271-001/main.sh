# Использование Spring Initializr через командную строку (пример)
curl https://start.spring.io/starter.zip \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d baseDir=my-first-spring-app \
  -d groupId=com.example \
  -d artifactId=demo \
  -d name=demo \
  -d packageName=com.example.demo \
  -d dependencies=web,lombok \
  -o demo.zip

unzip demo.zip
cd demo
