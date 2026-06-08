type User = { id: string; name: string };

async function* fetchUsers(url: string): AsyncGenerator<User> {
  let page = 1;
  let hasMore = true;
  while (hasMore) {
    const res = await fetch(`${url}?page=${page}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const body = (await res.json()) as { items: User[]; hasMore: boolean };
    for (const user of body.items) {
      yield user;
    }
    hasMore = body.hasMore;
    page += 1;
  }
}

async function printAll(): Promise<void> {
  for await (const user of fetchUsers("/api/users")) {
    console.log(user.name);
  }
}
