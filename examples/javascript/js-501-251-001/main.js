> const asyncIterable = {
>   [Symbol.asyncIterator]() {
>     let i = 0;
>     return {
>       next() {
>         return Promise.resolve(i < 3 ? { value: i++, done: false } : { done: true });
>       }
>     };
>   }
> };
> 
> (async () => {
>   for await (const x of asyncIterable) console.log(x); // 0, 1, 2
> })();
> 