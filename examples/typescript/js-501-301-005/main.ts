type Role = 'user' | 'admin';
type UserTuple = readonly [id: string, role: Role];

interface UserProfile {
  id: string;
  email: string;
  tags?: string[];
}

enum Access {
  Read = 'READ',
  Write = 'WRITE'
}

const printProfile = (profile: UserProfile, ...notes: string[]): void => {
  console.log(profile.email, notes.join(', '));
};
