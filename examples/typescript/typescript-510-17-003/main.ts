type Dashboard = {
  user: User;
  notifications: { id: string; text: string }[];
};

async function loadDashboard(userId: string): Promise<Dashboard> {
  const [user, notifications] = await Promise.all([
    loadUser(userId),
    loadNotifications(userId),
  ]);
  return { user, notifications };
}

async function loadNotifications(
  userId: string,
): Promise<{ id: string; text: string }[]> {
  const res = await fetch(`/api/notifications/${userId}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const raw: unknown = await res.json();
  if (!Array.isArray(raw)) throw new Error("Ожидался массив");
  return raw as { id: string; text: string }[];
}
