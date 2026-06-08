// Интерфейс для пропсов компонента
interface CardProps {
  title: string;
  description: string;
}

// Компонент с проверкой типов
function Card({ title, description }: CardProps) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <p>{description}</p>
    </div>
  );
}

// Использование компонента
<Card 
  title="Заголовок" 
  description="Описание контента" 
/>
