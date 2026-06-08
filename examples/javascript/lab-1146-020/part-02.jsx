import { ThemeProvider, useTheme } from './theme/ThemeContext';

function Toolbar() {
  const { theme, toggle } = useTheme();
  return (
    <button type="button" onClick={toggle}>
      Тема: {theme}
    </button>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <Toolbar />
      <main>Контент страницы</main>
    </ThemeProvider>
  );
}
