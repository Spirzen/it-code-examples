# --- Стадия сборки ---
FROM golang:1.22 AS build
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /app/server .

# --- Финальный образ ---
FROM alpine:3.19
WORKDIR /app
COPY --from=build /app/server .
USER 65532:65532
CMD ["./server"]
