const asyncRange = {
    from: 1,
    to: 3,
    
    async *[Symbol.asyncIterator]() {
        for (let i = this.from; i <= this.to; i++) {
            await new Promise(resolve => setTimeout(resolve, 1000));
            yield i;
        }
    }
};

// Использование асинхронного итератора
(async () => {
    for await (let num of asyncRange) {
        console.log(num); // 1 (через 1с), 2 (через 2с), 3 (через 3с)
    }
})();
