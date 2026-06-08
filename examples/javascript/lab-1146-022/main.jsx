import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { Hero } from './components/sections/Hero';
import { Features } from './components/sections/Features';
import { Faq } from './components/sections/Faq';

export default function App() {
  return (
    <>
      <Header />
      <main>
        <Hero />
        <Features />
        <Faq />
      </main>
      <Footer />
    </>
  );
}
