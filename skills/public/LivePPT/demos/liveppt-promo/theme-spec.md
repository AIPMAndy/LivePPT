# LivePPT Promo Theme Spec

## Theme Identity

- Theme name: ivory-luxe
- Tone keywords: premium, bright, restrained, luxury editorial
- Suitable scenarios: GitHub 项目发布、B 端方案路演、技术产品介绍

## Token Values

- `--color-bg`: `#f8f4ee`
- `--color-surface`: `rgba(255, 251, 245, 0.92)`
- `--color-text`: `#2d2115`
- `--color-accent`: `#b58a52`
- `--motion-primary`: `cubic-bezier(0.2, 0.9, 0.2, 1)`
- `--radius-card`: `14px`
- `--shadow-elevated`: `0 24px 60px rgba(109, 79, 47, 0.20)`

## Typography

- Heading font: Bodoni MT / Didot / Songti SC
- Body font: Avenir Next / PingFang SC / Microsoft YaHei
- Number font: Bodoni MT / Avenir Next (700)

## Motion

- Scene transition: short directional slide-in (520ms)
- Element entrance: content first, metrics second
- Hover feedback: gold border glow + soft metallic accent background

## Accessibility Checks

- Contrast pass: dark theme & light theme both maintain readable contrast
- Reduced motion variant: disabled transitions under `prefers-reduced-motion`
- Keyboard navigation pass: `←`/`→`/`Home`/`End` supported
