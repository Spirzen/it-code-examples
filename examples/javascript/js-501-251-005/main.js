> // В основном потоке:
> const sab = new SharedArrayBuffer(4);
> const ia = new Int32Array(sab);
> ia[0] = 0;
> worker.postMessage({ sab });
> 
> // В Worker:
> self.onmessage = e => {
>   const ia = new Int32Array(e.Data.sab);
>   Atomics.wait(ia, 0, 0); // ждёт, пока ia[0] ≠ 0
>   console.log('Разрешено');
> };
> 
> // Позже в основном потоке:
> Atomics.store(ia, 0, 1);
> Atomics.notify(ia, 0);
> 