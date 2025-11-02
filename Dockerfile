# Etapa 1 — imagem base com Java 17 (leve e segura)
FROM eclipse-temurin:17-jdk AS runtime

# Define o diretório de trabalho
WORKDIR /app

# Copia o JAR da aplicação (gerado pelo Maven)
COPY target/*.jar app.jar

# Porta padrão do Spring Boot
EXPOSE 8080

# Variáveis de ambiente úteis
ENV JAVA_OPTS=""

# Comando para executar o app
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]