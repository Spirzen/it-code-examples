/**
 * Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3
 * Вместо реального HTTP — sleep, чтобы сравнить время без сети.
 */

const downloads = [
  { url: 'https://example.com/page1', delayMs: 2000 },
  { url: 'https://example.com/page2', delayMs: 3500 },
  { url: 'https://example.com/page3', delayMs: 1500 },
  { url: 'https://example.com/page4', delayMs: 2500 },
  { url: 'https://example.com/page5', delayMs: 1000 },
];

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchSimulated(url, delayMs) {
  await sleep(delayMs);
  return { url, ok: true };
}

async function sequential(items) {
  console.log('\n1. ПОСЛЕДОВАТЕЛЬНО (await в цикле)');
  const start = performance.now();
  for (const { url, delayMs } of items) {
    await fetchSimulated(url, delayMs);
    console.log(`  Готово: ${url}`);
  }
  const elapsed = (performance.now() - start) / 1000;
  console.log(`  Время: ${elapsed.toFixed(2)} с`);
  return elapsed;
}

async function parallel(items) {
  console.log('\n2. ПАРАЛЛЕЛЬНО (Promise.all)');
  const start = performance.now();
  await Promise.all(
    items.map(async ({ url, delayMs }) => {
      await fetchSimulated(url, delayMs);
      console.log(`  Готово: ${url}`);
    }),
  );
  const elapsed = (performance.now() - start) / 1000;
  console.log(`  Время: ${elapsed.toFixed(2)} с`);
  return elapsed;
}

function cpuInMainThread(n) {
  let sum = 0;
  for (let i = 0; i < n; i++) sum += i;
  return sum;
}

async function demonstrateWorker() {
  if (typeof Worker === 'undefined') {
    console.log('\n3. worker_threads — только в Node.js');
    return;
  }

  const { Worker, isMainThread, parentPort, workerData } = await import('node:worker_threads');

  if (!isMainThread) {
    let sum = 0;
    for (let i = 0; i < workerData.n; i++) sum += i;
    parentPort.postMessage(sum);
    return;
  }

  console.log('\n3. CPU в Node.js — worker_threads');
  const start = performance.now();
  const sum = await new Promise((resolve, reject) => {
    const worker = new Worker(new URL(import.meta.url), {
      workerData: { n: 10_000_000 },
    });
    worker.on('message', resolve);
    worker.on('error', reject);
  });
  const elapsed = (performance.now() - start) / 1000;
  console.log(`  Сумма: ${sum}, время: ${elapsed.toFixed(2)} с`);
}

async function main() {
  console.log('=== JavaScript — sequential vs Promise.all ===');

  const seq = await sequential(downloads);
  const par = await parallel(downloads);

  console.log('\n--- Итог ---');
  console.log(`Последовательно: ${seq.toFixed(2)} с`);
  console.log(`Promise.all:     ${par.toFixed(2)} с`);
  console.log(`Ускорение:       ${(seq / par).toFixed(2)}x`);

  await demonstrateWorker();
}

main().catch(console.error);
