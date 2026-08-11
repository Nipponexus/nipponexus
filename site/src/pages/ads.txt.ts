import { ADSENSE_PUB_ID } from '../config/ads';
export const GET = () => {
  const id = ADSENSE_PUB_ID.replace(/^ca-/, '');
  const body = id ? `google.com, ${id}, DIRECT, f08c47fec0942fa0\n` : '';
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
