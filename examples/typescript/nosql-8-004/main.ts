   import { serialize, deserialize } from 'some-serializer'; // например, msgpack

   export class SessionService {
     async getSession(token: string): Promise<Session | null> {
       const key = `sess:${token}`;
       try {
         const data = await memcached.get(key);
         if (!data) return null;

         return deserialize(data) as Session;
       } catch (err) {
         // Логируем, но не прерываем — попробуем БД (если есть резерв)
         console.warn('Cache miss or error for session', token, err);
         return null;
       }
     }

     async createSession(session: Session): Promise<string> {
       const token = crypto.randomBytes(24).toString('hex');
       const key = `sess:${token}`;
       const serialized = serialize(session);

       // TTL = 24 часа (в секундах)
       await memcached.set(key, serialized, 86400);
       return token;
     }

     async invalidateSession(token: string): Promise<void> {
       await memcached.del(`sess:${token}`).catch(() => {
         // Игнорируем ошибки удаления — сессия и так умрёт по TTL
       });
     }
   }
