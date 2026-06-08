const size_t n_threads = std::thread::hardware_concurrency();
const size_t chunk = (N + n_threads - 1) / n_threads;  // ceil(N / n_threads)

std::vector<std::thread> threads;
for (size_t t = 0; t < n_threads; ++t) {
    size_t start = t * chunk;
    size_t end = std::min(start + chunk, N);
    threads.emplace_back([&, start, end]{
        for (size_t i = start; i < end; ++i) {
            compute(i);
        }
    });
}
for (auto& th : threads) th.join();
