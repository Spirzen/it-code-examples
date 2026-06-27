import {loadEcosystemConfig, buildNavItems, resolvePortalBase} from './ecosystem.mjs';

export function getPortalContext() {
  const config = loadEcosystemConfig({dev: import.meta.env.DEV});
  return {
    config,
    navItems: buildNavItems(config, 'code'),
    brandHref: resolvePortalBase(config, 'code'),
    brandLabel: 'Код IT',
    ecosystemConfigJson: JSON.stringify({
      postMessage: config.postMessage,
      domains: config.domains,
    }),
  };
}
