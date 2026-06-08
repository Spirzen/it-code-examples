import { BrowserRouter, Link, NavLink, Route, Routes } from 'react-router-dom';

function Home() {
  return <h1>Главная</h1>;
}

function About() {
  return <h1>О проекте</h1>;
}

function NotFound() {
  return <h1>404 — страница не найдена</h1>;
}

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Главная</Link>
        {' · '}
        <NavLink to="/about">О нас</NavLink>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
