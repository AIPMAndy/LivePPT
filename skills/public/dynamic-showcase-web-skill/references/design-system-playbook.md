# Design System Playbook

## 1. Layout Rules

- One scene = one core message.
- Keep clear hierarchy: title, proof point, supporting detail, CTA.
- Use 12-column grid on desktop and 4-column grid on mobile.

## 2. Typography Rules

- Maximum two font families per theme.
- Heading scale suggestion: 56 / 40 / 28 / 20.
- Body text line length target: 28-42 Chinese characters.

## 3. Motion Rules

- Default transition duration: 350-700ms.
- Layered entrance order: background -> content -> CTA.
- Avoid simultaneous heavy blur, scale, and parallax on low-end devices.

## 4. Accessibility Rules

- Color contrast target: WCAG AA.
- Respect `prefers-reduced-motion` and disable non-essential animations.
- Keyboard navigation support is required for scene switching.

## 5. Performance Rules

- Compress media assets and avoid oversized videos.
- Defer non-critical animations until first interaction.
- Keep initial payload lean and prioritize above-the-fold content.
