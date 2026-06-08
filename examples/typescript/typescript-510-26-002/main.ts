@Entity("posts")
export class Post {
  @PrimaryGeneratedColumn("uuid")
  id!: string;

  @Column()
  title!: string;

  @ManyToOne(() => User, (user) => user.posts)
  author!: User;
}

@Entity("users")
export class User {
  @PrimaryGeneratedColumn("uuid")
  id!: string;

  @OneToMany(() => Post, (post) => post.author)
  posts!: Post[];
}
