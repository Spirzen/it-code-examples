type AnalyticsService struct {
    queue chan *http.Request
    done  chan struct{}
}

func (s *AnalyticsService) Start() {
    for i := 0; i < 4; i++ {
        go s.worker()
    }
}

func (s *AnalyticsService) Enqueue(r *http.Request) {
    select {
    case s.queue <- r:
    default:
        // очередь переполнена — отбрасываем или логируем
    }
}

func (s *AnalyticsService) Stop() {
    close(s.queue)
    <-s.done
}
