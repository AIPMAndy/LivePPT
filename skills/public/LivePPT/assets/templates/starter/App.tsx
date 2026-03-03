import React, {useEffect, useMemo, useState} from "react";

import "./styles.css";

type ThemeName = "prism-command" | "linen-editorial" | "signal-night";

interface Metric {
  label: string;
  value: string;
  note: string;
}

interface Scene {
  id: string;
  kicker: string;
  title: string;
  body: string;
  insight: string;
  metrics: Metric[];
}

const SCENES: Scene[] = [
  {
    id: "scene-01",
    kicker: "Narrative Start",
    title: "Turn linear slides into decision-ready web stories",
    body: "LivePPT keeps the same narrative spine while delivering click-through interactions and scene-level pacing.",
    insight: "One scene carries one decision signal.",
    metrics: [
      {label: "Screens", value: "8", note: "Core flow"},
      {label: "Themes", value: "3", note: "Runtime switch"},
      {label: "Cycle", value: "7d", note: "MVP launch"},
    ],
  },
  {
    id: "scene-02",
    kicker: "Problem",
    title: "Why traditional decks break in real demos",
    body: "Static pages cannot adapt to stakeholder questions, and visual changes often require rebuilding the whole deck.",
    insight: "High polish fails when interaction is missing.",
    metrics: [
      {label: "Rework", value: "42%", note: "Visual-only edits"},
      {label: "Handover", value: "Slow", note: "Hard to reuse"},
      {label: "Risk", value: "High", note: "Demo inconsistency"},
    ],
  },
  {
    id: "scene-03",
    kicker: "Solution",
    title: "A structured scene engine with tokenized themes",
    body: "Content, structure, and style are separated. Teams can preserve message flow while switching visual identity in seconds.",
    insight: "Stable structure, flexible presentation.",
    metrics: [
      {label: "Modes", value: "Click / Key", note: "Dual navigation"},
      {label: "Tokens", value: "Color + Motion", note: "Design system"},
      {label: "QA", value: "Built-in", note: "Validation command"},
    ],
  },
  {
    id: "scene-04",
    kicker: "CTA",
    title: "Ship one polished showcase this week",
    body: "Use the starter, swap your copy, choose a theme, and publish a live demo with changelog-backed release notes.",
    insight: "From brief to public demo in one workflow.",
    metrics: [
      {label: "Output", value: "Demo URL", note: "Public-ready"},
      {label: "Docs", value: "Complete", note: "Contribute friendly"},
      {label: "Launch", value: "v0.1", note: "Open source"},
    ],
  },
];

const THEMES: Array<{name: ThemeName; label: string}> = [
  {name: "prism-command", label: "Prism Command"},
  {name: "linen-editorial", label: "Linen Editorial"},
  {name: "signal-night", label: "Signal Night"},
];

const nextIndex = (current: number, delta: number, total: number): number => {
  const index = current + delta;
  if (index < 0) {
    return 0;
  }

  if (index > total - 1) {
    return total - 1;
  }

  return index;
};

const App: React.FC = () => {
  const [sceneIndex, setSceneIndex] = useState(0);
  const [theme, setTheme] = useState<ThemeName>("prism-command");

  const activeScene = SCENES[sceneIndex];
  const progress = useMemo(
    () => ((sceneIndex + 1) / SCENES.length) * 100,
    [sceneIndex],
  );

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "ArrowRight") {
        setSceneIndex((prev) => nextIndex(prev, 1, SCENES.length));
      }

      if (event.key === "ArrowLeft") {
        setSceneIndex((prev) => nextIndex(prev, -1, SCENES.length));
      }

      if (event.key === "Home") {
        setSceneIndex(0);
      }

      if (event.key === "End") {
        setSceneIndex(SCENES.length - 1);
      }
    };

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

  return (
    <div className="lp-root" data-theme={theme}>
      <div className="lp-bg-orb lp-bg-orb--one" />
      <div className="lp-bg-orb lp-bg-orb--two" />
      <div className="lp-noise" />

      <header className="lp-topbar">
        <div className="lp-brand">
          <span className="lp-brand-chip">LivePPT</span>
          <span className="lp-brand-text">Distinct Showcase Starter</span>
        </div>

        <label className="lp-theme-switch" htmlFor="theme-switch">
          <span>Theme</span>
          <select
            id="theme-switch"
            value={theme}
            onChange={(event) => setTheme(event.target.value as ThemeName)}
          >
            {THEMES.map((option) => (
              <option key={option.name} value={option.name}>
                {option.label}
              </option>
            ))}
          </select>
        </label>
      </header>

      <main className="lp-main">
        <aside className="lp-rail" aria-label="Scene navigation">
          {SCENES.map((scene, index) => (
            <button
              key={scene.id}
              type="button"
              className={`lp-rail-item ${index === sceneIndex ? "is-active" : ""}`}
              onClick={() => setSceneIndex(index)}
            >
              <span className="lp-rail-dot" />
              <span className="lp-rail-label">{scene.kicker}</span>
            </button>
          ))}
        </aside>

        <section className="lp-stage" aria-live="polite">
          <article key={activeScene.id} className="lp-scene-card lp-scene-enter">
            <p className="lp-kicker">{activeScene.kicker}</p>
            <h1>{activeScene.title}</h1>
            <p className="lp-body">{activeScene.body}</p>
            <p className="lp-insight">{activeScene.insight}</p>
          </article>

          <div className="lp-metric-grid">
            {activeScene.metrics.map((metric) => (
              <div key={metric.label} className="lp-metric-card">
                <div className="lp-metric-label">{metric.label}</div>
                <div className="lp-metric-value">{metric.value}</div>
                <div className="lp-metric-note">{metric.note}</div>
              </div>
            ))}
          </div>
        </section>
      </main>

      <footer className="lp-footer">
        <div className="lp-progress-wrap" role="progressbar" aria-valuenow={sceneIndex + 1} aria-valuemin={1} aria-valuemax={SCENES.length}>
          <div className="lp-progress-track">
            <div className="lp-progress-fill" style={{width: `${progress}%`}} />
          </div>
          <span className="lp-progress-text">
            {sceneIndex + 1} / {SCENES.length}
          </span>
        </div>

        <div className="lp-controls">
          <button
            type="button"
            onClick={() => setSceneIndex((prev) => nextIndex(prev, -1, SCENES.length))}
            disabled={sceneIndex === 0}
          >
            Previous
          </button>
          <button
            type="button"
            onClick={() => setSceneIndex((prev) => nextIndex(prev, 1, SCENES.length))}
            disabled={sceneIndex === SCENES.length - 1}
          >
            Next
          </button>
        </div>
      </footer>
    </div>
  );
};

export default App;
