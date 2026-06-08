input {
  http {
    port => 8080
    codec => json
  }
}

filter {
  mutate {
    add_field => { "received_at" => "%{@timestamp}" }
  }
}

output {
  kafka {
    bootstrap_servers => "kafka:9092"
    topic_id => "incoming-events"
    compression_type => "snappy"
  }
}
