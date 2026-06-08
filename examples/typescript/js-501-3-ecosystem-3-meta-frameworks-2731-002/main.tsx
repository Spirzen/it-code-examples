
import { TopNav } from '@/components/layout/TopNav';
import { SiteFooter } from '@/components/layout/SiteFooter';
import { WelcomeBlock } from '@/components/sections/WelcomeBlock';
import { ConfidenceLine } from '@/components/sections/ConfidenceLine';
import { RoadmapBlock } from '@/components/sections/RoadmapBlock';
import { FeatureGrid } from '@/components/sections/FeatureGrid';
import { ReviewsBlock } from '@/components/sections/ReviewsBlock';
import { PlansBlock } from '@/components/sections/PlansBlock';
import { HelpCenterBlock } from '@/components/sections/HelpCenterBlock';
import { ActionBlock } from '@/components/sections/ActionBlock';

export default function HomePage() {
  return (
    <>
      <TopNav />
      <main>
        <WelcomeBlock />
        <ConfidenceLine />
        <RoadmapBlock />
        <FeatureGrid />
        <ReviewsBlock />
        <PlansBlock />
        <HelpCenterBlock />
        <ActionBlock />
      </main>
      <SiteFooter />
    </>
  );
}
