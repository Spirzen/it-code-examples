type CardProps = {
  title: string;
  subtitle?: string;
  children?: React.ReactNode;
};

function Card({ title, subtitle, children }: CardProps) {
  return (
    <section className="card">
      <h2>{title}</h2>
      {subtitle ? <p>{subtitle}</p> : null}
      {children}
    </section>
  );
}
