import axios from 'axios';

async function getAccessToken(): Promise<string> {
  const { data } = await axios.post(
    'https://auth.example.com/oauth/token',
    new URLSearchParams({
      grant_type: 'client_credentials',
      client_id: process.env.CLIENT_ID!,
      client_secret: process.env.CLIENT_SECRET!,
      scope: 'orders:import',
    }),
    { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } },
  );
  return data.access_token;
}

const api = axios.create({ baseURL: 'https://api.example.com' });
api.interceptors.request.use(async (config) => {
  config.headers.Authorization = `Bearer ${await getAccessToken()}`;
  return config;
});
