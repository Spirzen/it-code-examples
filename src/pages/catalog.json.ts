import type {APIRoute} from 'astro';
import {loadCatalog} from '@/lib/examples';

export const GET: APIRoute = () => {
  return new Response(JSON.stringify(loadCatalog()), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
