import type {APIRoute} from 'astro';
import {groupByLanguage, loadCatalog} from '@/lib/examples';

export function getStaticPaths() {
  const grouped = groupByLanguage(loadCatalog());
  return [...grouped.keys()].map((lang) => ({
    params: {lang},
  }));
}

export const GET: APIRoute = ({params}) => {
  const lang = params.lang as string;
  const items = groupByLanguage(loadCatalog()).get(lang) ?? [];
  return new Response(JSON.stringify(items), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
