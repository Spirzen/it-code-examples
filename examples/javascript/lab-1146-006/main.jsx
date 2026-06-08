import { useEffect, useState } from 'react';
import { CardSkeleton } from './CardSkeleton';

export function ProfileCard() {
  const [status, setStatus] = useState('loading');
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const timer = setTimeout(() => {
      setProfile({ name: 'Анна', role: 'Frontend-разработчик' });
      setStatus('ok');
    }, 1000);
    return () => clearTimeout(timer);
  }, []);

  if (status === 'loading') return <CardSkeleton />;
  if (!profile) return <p className="error">Нет данных</p>;

  return (
    <article className="profile-card">
      <h2>{profile.name}</h2>
      <p>{profile.role}</p>
    </article>
  );
}
