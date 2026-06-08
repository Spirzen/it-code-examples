FROM debian:bookworm-slim
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Редко меняется — выше в файле
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Часто меняется — ближе к концу
COPY target/app.jar ./app.jar

RUN useradd -m -r appuser
USER appuser

LABEL maintainer="team@example.com" \
      version="1.4.2" \
      description="Payment API"

CMD ["java", "-jar", "app.jar"]
