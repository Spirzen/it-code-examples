
import { MainHeader } from '@/components/layout/MainHeader';
import { MainFooter } from '@/components/layout/MainFooter';
import { HeroBlock } from '@/components/sections/HeroBlock';
import { AdvantageBlock } from '@/components/sections/AdvantageBlock';
import { ProcessBlock } from '@/components/sections/ProcessBlock';
import { ProofBlock } from '@/components/sections/ProofBlock';
import { CostBlock } from '@/components/sections/CostBlock';
import { HelpBlock } from '@/components/sections/HelpBlock';
import { StartBlock } from '@/components/sections/StartBlock';

export default function HomePage() {
  return (
    <>
      <MainHeader />
      <main>
        <HeroBlock />
        <AdvantageBlock />
        <ProcessBlock />
        <ProofBlock />
        <CostBlock />
        <HelpBlock />
        <StartBlock />
      </main>
      <MainFooter />
    </>
  );
}
