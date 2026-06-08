> async function* fetchPages(url) {
>   let page = 1;
>   while (true) {
>     const res = await fetch(`$\&#123;url\&#125;?page=$&#123;page&#125;`);
>     const data = await res.json();
>     if (data.items.length === 0) return;
>     yield data.items;
>     page++;
>   }
> }
> 
> (async () => {
>   for await (const items of fetchPages('/api/data')) {
>     console.log(items);
>   }
> })();
> 