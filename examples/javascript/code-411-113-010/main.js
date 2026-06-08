// Performance Observer для отслеживания ключевых метрик
const observer = new PerformanceObserver((list) => {
    const entries = list.getEntries();
    entries.forEach(entry => {
        const metric = {
            name: entry.name,
            type: entry.entryType,
            duration: entry.duration,
            startTime: entry.startTime
        };
        window.bridge.call('reportMetric', metric);
    });
});

observer.observe({
    entryTypes: ['navigation', 'resource', 'paint', 'largest-contentful-paint']
});

// Измерение Core Web Vitals
const metrics = {
    fcp: 0,   // First Contentful Paint
    lcp: 0,   // Largest Contentful Paint
    cls: 0,   // Cumulative Layout Shift
    fid: 0,   // First Input Delay
    inp: 0    // Interaction to Next Paint
};

new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (entry.entryType === 'largest-contentful-paint') {
            metrics.lcp = entry.renderTime || entry.loadTime;
        }
    }
}).observe({ type: 'largest-contentful-paint', buffered: true });
