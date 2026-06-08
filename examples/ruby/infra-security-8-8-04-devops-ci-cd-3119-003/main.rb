input {
  beats {
    port => 5044
  }
}

filter {
  if [log][level] == "error" {
    clone {
      clones => ["archive"]
      add_tag => ["archived_error"]
    }
  }
}

output {
  if "archived_error" in [tags] {
    file {
      path => "/var/log/errors-archive/%{+YYYY-MM-dd}.log"
      codec => json_lines
    }
  }

  elasticsearch {
    hosts => ["http://es:9200"]
    index => "logs-%{[@metadata][beat]}-%{+YYYY.MM.dd}"
  }
}
