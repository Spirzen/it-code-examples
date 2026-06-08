
import { TopBar } from './components/layout/TopBar';
import { BottomBar } from './components/layout/BottomBar';
import { IntroSection } from './components/sections/IntroSection';
import { ValueStrip } from './components/sections/ValueStrip';
import { BenefitsSection } from './components/sections/BenefitsSection';
import { WorkflowSection } from './components/sections/WorkflowSection';
import { TrustSection } from './components/sections/TrustSection';
import { PriceSection } from './components/sections/PriceSection';
import { QuestionsSection } from './components/sections/QuestionsSection';
import { FinalAction } from './components/sections/FinalAction';

export default function App() {
  return (
    <>
      <TopBar />
      <main>
        <IntroSection />
        <ValueStrip />
        <BenefitsSection />
        <WorkflowSection />
        <TrustSection />
        <PriceSection />
        <QuestionsSection />
        <FinalAction />
      </main>
      <BottomBar />
    </>
  );
}
