const repo = "https://github.com/AIPMAndy/LivePPT";

const slides = [
  {
    nav: "开场",
    type: "cover",
    title: "LivePPT：让你的 GitHub 项目，像发布会一样被看见",
    highlight: "动态PPT，不只是排版，是传播效率",
    subtitle:
      "你不需要复杂框架，也不需要重做一套前端。用 LivePPT，把 README 里的价值转成可点击、可演示、可传播的故事线。",
    script:
      "过去我们只会写 README；现在我们要会“演”README。LivePPT 的目标，就是让项目价值在 60 秒内被看懂、被记住、被转发。",
  },
  {
    nav: "痛点",
    type: "pain",
    title: "项目推广经常卡在这三步",
    highlight: "内容有了，但表达弱了",
    cards: [
      {
        icon: "🧱",
        title: "信息堆叠，没有镜头感",
        body: "README 信息很全，但没有节奏推进。用户看完仍说不清你到底解决了什么问题。",
      },
      {
        icon: "🎨",
        title: "换风格就要重做页面",
        body: "想换视觉就动结构，维护成本暴涨。一次发布会风格，无法复用到下次内容。",
      },
      {
        icon: "📉",
        title: "传播链路断裂",
        body: "读文档的人多，真正留下来的人少。项目没有形成第一眼记忆点，转化自然低。",
      },
    ],
    script:
      "很多项目不是技术不行，而是表达方式不够强。用户看懂你的仓库，不代表用户愿意帮你传播仓库。",
  },
  {
    nav: "方案",
    type: "split",
    tag: "LivePPT Method",
    title: "先定叙事骨架，再切视觉主题",
    subtitle:
      "LivePPT 把结构、文案、主题做了解耦。你可以一套内容跑多个场景：项目发布、技术分享、课程讲解、客户提案。",
    bullets: [
      "Scene Map：拆解逐页叙事，控制信息密度",
      "Theme Layer：换肤不改内容，品牌延续稳定",
      "Runtime Controls：点击、键盘、自动播放三种节奏",
    ],
    terminal: [
      { type: "muted", text: "# 把文档升级为演示体验" },
      { type: "cmd", text: "$ liveppt create --from README.md --theme ivory-luxe" },
      { type: "muted", text: "> parsing sections..." },
      { type: "muted", text: "> mapping scenes..." },
      { type: "muted", text: "> generating interactive deck..." },
      { type: "good", text: "✅ Done. open ./demos/liveppt-promo/index.html" },
      { type: "note", text: "Tip: press Space / → to keep presentation flow." },
    ],
    script:
      "这一页的重点是：LivePPT 不只是模板，而是一套可复用的叙事工程。你的内容资产会越做越轻松，而不是每次重做。",
  },
  {
    nav: "演示",
    type: "simulator",
    title: "交互演示：给项目一键装上发布会模板",
    subtitle: "点击右侧按钮，体验模板安装与日志输出。",
    templates: [
      {
        id: "launch",
        name: "发布会主视觉模板",
        command: "liveppt add-template launch-premium",
      },
      {
        id: "product",
        name: "产品演示增长模板",
        command: "liveppt add-template product-growth",
      },
      {
        id: "investor",
        name: "融资路演叙事模板",
        command: "liveppt add-template investor-story",
      },
    ],
    script:
      "这个小模拟器体现的是交付体验：不是交给用户一堆文件，而是让用户“感觉自己已经会用了”。这是传播转化的关键。",
  },
  {
    nav: "组成",
    type: "modules",
    title: "一个高质量 LivePPT Skill，至少包含三层能力",
    modules: [
      {
        tone: "blue",
        title: "Story Engine",
        body: "把线性文档转成分镜结构：封面、冲突、解法、案例、行动召唤，避免信息一股脑灌输。",
      },
      {
        tone: "indigo",
        title: "Theme Tokens",
        body: "颜色、字号、间距、圆角、动效全部令牌化。换主题时不破坏结构和文案，风格切换更稳定。",
      },
      {
        tone: "purple",
        title: "Delivery Controls",
        body: "支持点按翻页、键盘控制、自动播放、进度条和提示脚本。你可以专注讲述，而不是操作界面。",
      },
    ],
    script:
      "真正能落地的 Skill，不是只有漂亮皮肤。它必须同时解决叙事结构、视觉系统和演示控制这三层问题。",
  },
  {
    nav: "场景",
    type: "usecase",
    title: "LivePPT 的真实高频应用场景",
    subtitle: "同一套项目内容，可以被讲给完全不同的人听。",
    cases: [
      {
        title: "开源发布",
        body: "新版本上线时，把更新点做成 7 页可点击发布会，用户更愿意看完并 Star。",
      },
      {
        title: "售前提案",
        body: "面向客户演示解决方案，用分镜一步步建立信任，而不是甩一页大表格。",
      },
      {
        title: "课程内容",
        body: "把知识点拆成节奏化页面，讲师控场更稳，学员记忆点更清晰。",
      },
    ],
    terminal: [
      { type: "muted", text: "# distribution checklist" },
      { type: "good", text: "1) Publish demo page" },
      { type: "good", text: "2) Attach in README + release notes" },
      { type: "good", text: "3) Share on X / 社区 / 技术群" },
      { type: "note", text: "Result: 更快理解 + 更高转发 + 更多参与" },
    ],
    script:
      "你会发现 LivePPT 最强的一点，是一稿多用。不是每次换场景都重做素材，而是同一资产持续放大价值。",
  },
  {
    nav: "总结",
    type: "summary",
    title: "现在就把你的仓库，升级成 LivePPT 发布会",
    points: [
      "保留你的技术深度，但换一种更容易被理解的表达方式。",
      "用分镜讲述代替信息平铺，让用户在短时间内记住核心价值。",
      "让 README、Demo、发布会形成统一传播链路，持续提升 Star/Fork/PR。",
    ],
    script:
      "最后一句：先被看见，才会被使用。LivePPT 不是为了漂亮，而是为了把你的项目价值更快传递给对的人。",
  },
];

const simulatorState = {
  installed: new Set(),
  installing: null,
  logs: [],
  timers: [],
};

const SIMULATOR_INSTALL_STEPS = [
  { delay: 980, text: "> Resolving assets from LivePPT template registry...", type: "muted" },
  { delay: 1880, text: "> Injecting storytelling blocks and motion presets...", type: "muted" },
  { delay: 2960, text: "> Applying luxury-tone style tokens and CTA components...", type: "muted" },
  { delay: 4040, text: "✅ {templateName} 安装完成", type: "ok" },
  {
    delay: 4700,
    text: "> Ready: this template is now available in your next deck.",
    type: "ok",
    done: true,
  },
];

const app = document.getElementById("app");
const slideRoot = document.getElementById("slideRoot");
const scriptFooter = document.getElementById("scriptFooter");
const progressBar = document.getElementById("progressBar");
const stepHint = document.getElementById("stepHint");
const dotNav = document.getElementById("dotNav");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const playBtn = document.getElementById("playBtn");

let current = 0;
let autoTimer = null;

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderTerminal(lines, title = "liveppt.log") {
  const content = lines
    .map((line) => `<div class="line-${line.type ?? "muted"}">${escapeHtml(line.text)}</div>`)
    .join("");

  return `
    <div class="terminal-card">
      <div class="terminal-head">
        <span class="term-dot red"></span>
        <span class="term-dot yellow"></span>
        <span class="term-dot green"></span>
        <span class="term-title">${escapeHtml(title)}</span>
      </div>
      <div class="terminal-body">${content}</div>
    </div>
  `;
}

function getTemplateButtonState(templateId) {
  const installed = simulatorState.installed.has(templateId);
  const loading = simulatorState.installing === templateId;
  const disabled = installed || simulatorState.installing !== null;

  if (installed) {
    return {
      className: "template-btn is-installed",
      label: "Installed",
      disabled,
      installed,
    };
  }

  if (loading) {
    return {
      className: "template-btn is-loading",
      label: "Installing...",
      disabled,
      installed,
    };
  }

  return {
    className: "template-btn",
    label: "Get",
    disabled,
    installed,
  };
}

function renderCover(scene) {
  return `
    <section class="slide-shell scene-enter">
      <div class="hero-grid">
        <div class="hero-left">
          <div class="hero-meta">
            <span class="meta-pill">LivePPT Skill</span>
            <span class="meta-pill indigo">项目推广动态演示</span>
          </div>
          <h1 class="hero-title">${escapeHtml(scene.title)}<br/><span>${escapeHtml(scene.highlight)}</span></h1>
          <p class="hero-sub">${escapeHtml(scene.subtitle)}</p>
          <div class="hero-actions">
            <a class="action-btn primary" href="${repo}" target="_blank" rel="noreferrer">⭐ 查看 GitHub 仓库</a>
            <a class="action-btn secondary" href="${repo}/tree/main/demos/liveppt-promo" target="_blank" rel="noreferrer">🎬 查看 Demo 源码</a>
          </div>
        </div>

        <div class="hero-right">
          <div class="hero-logo-card">
            <div class="logo-mark">LP</div>
            <div class="logo-label">LivePPT Dynamic Deck</div>
          </div>
          <div class="hero-float-badge">CN · Growth Ready</div>
        </div>
      </div>
    </section>
  `;
}

function renderPain(scene) {
  const cards = scene.cards
    .map(
      (card) => `
      <article class="info-card">
        <div class="info-icon">${escapeHtml(card.icon)}</div>
        <h3 class="info-title">${escapeHtml(card.title)}</h3>
        <p class="info-text">${escapeHtml(card.body)}</p>
      </article>
    `,
    )
    .join("");

  return `
    <section class="slide-shell scene-enter">
      <div class="pain-header">
        <span class="section-tag">Pain Points</span>
        <h2 class="pain-title">${escapeHtml(scene.title)}<br/><span>${escapeHtml(scene.highlight)}</span></h2>
      </div>
      <div class="info-grid">${cards}</div>
    </section>
  `;
}

function renderSplit(scene) {
  const bulletHtml = scene.bullets.map((item) => `<li>${escapeHtml(item)}</li>`).join("");

  return `
    <section class="slide-shell scene-enter">
      <div class="split-grid">
        <div class="copy-column">
          <span class="section-tag">${escapeHtml(scene.tag)}</span>
          <h2 class="big-title">${escapeHtml(scene.title)}</h2>
          <p class="lead">${escapeHtml(scene.subtitle)}</p>
          <ul class="feature-list">${bulletHtml}</ul>
        </div>

        <div>
          ${renderTerminal(scene.terminal, "liveppt_engine.log")}
        </div>
      </div>
    </section>
  `;
}

function renderSimulator(scene) {
  const items = scene.templates
    .map((template) => {
      const button = getTemplateButtonState(template.id);

      return `
        <article class="template-item ${button.installed ? "is-installed" : ""}">
          <div class="template-main">
            <strong>${escapeHtml(template.name)}</strong>
            <span>${escapeHtml(template.command)}</span>
          </div>
          <button
            type="button"
            class="${button.className}"
            data-template-id="${escapeHtml(template.id)}"
            ${button.disabled ? "disabled" : ""}
          >${escapeHtml(button.label)}</button>
        </article>
      `;
    })
    .join("");

  const loadout = simulatorState.installed.size
    ? [...simulatorState.installed]
        .map((id) => scene.templates.find((template) => template.id === id))
        .filter(Boolean)
        .map((template) => `<span class="loadout-chip">✅ ${escapeHtml(template.name)}</span>`)
        .join("")
    : `<div class="loadout-empty">Agent 还没有安装模板，等待操作中...</div>`;

  const logs = simulatorState.logs.length
    ? `<div class="log-lines">${simulatorState.logs
        .map((line) => `<div class="log-line ${line.type}">${escapeHtml(line.text)}</div>`)
        .join("")}${
        simulatorState.installing ? `<div class="log-cursor">_</div>` : ""
      }</div>`
    : `<div class="log-empty">Waiting for template installation...</div>`;

  return `
    <section class="slide-shell scene-enter">
      <div class="pain-header simulator-header">
        <span class="section-tag">Live Simulator</span>
        <h2 class="pain-title simulator-title">${escapeHtml(scene.title)}</h2>
      </div>

      <div class="sim-grid">
        <section class="template-market" data-no-advance="true">
          <div class="market-head">
            <div class="market-logo">LP</div>
            <div>
              <h3>LivePPT Template Store</h3>
              <p>github.com/AIPMAndy/LivePPT</p>
            </div>
          </div>
          <div class="template-list">${items}</div>
        </section>

        <section class="status-panel" data-no-advance="true">
          <article class="agent-loadout">
            <div class="loadout-head">
              <strong>Live Deck Loadout</strong>
              <span class="online-badge">ONLINE</span>
            </div>
            <div class="loadout-items">${loadout}</div>
          </article>

          <article class="log-panel">
            ${renderTerminal([], "template_installer.log")}
          </article>
        </section>
      </div>

      <template id="simLogsTemplate">${logs}</template>
    </section>
  `;
}

function patchSimulatorLogs() {
  const panel = slideRoot.querySelector(".log-panel .terminal-body");
  const logsTemplate = slideRoot.querySelector("#simLogsTemplate");

  if (!panel || !logsTemplate) return;

  panel.innerHTML = logsTemplate.innerHTML;
}

function renderModules(scene) {
  const cards = scene.modules
    .map(
      (item) => `
      <article class="module-card ${escapeHtml(item.tone)}">
        <h3>${escapeHtml(item.title)}</h3>
        <p>${escapeHtml(item.body)}</p>
      </article>
    `,
    )
    .join("");

  return `
    <section class="slide-shell scene-enter">
      <div class="module-head">
        <span class="section-tag">Core Composition</span>
        <h2 class="module-title">${escapeHtml(scene.title)}</h2>
      </div>
      <div class="module-grid">${cards}</div>
    </section>
  `;
}

function renderUsecase(scene) {
  const caseHtml = scene.cases
    .map(
      (item, index) => `
      <article class="case-item">
        <div class="case-index">${String(index + 1).padStart(2, "0")}</div>
        <div class="case-copy">
          <h4>${escapeHtml(item.title)}</h4>
          <p>${escapeHtml(item.body)}</p>
        </div>
      </article>
    `,
    )
    .join("");

  return `
    <section class="slide-shell scene-enter">
      <div class="usecase-grid">
        <div>
          <span class="section-tag">Use Cases</span>
          <h2 class="big-title usecase-title">${escapeHtml(scene.title)}</h2>
          <p class="lead usecase-subtitle">${escapeHtml(scene.subtitle)}</p>
          <div class="case-list">${caseHtml}</div>
        </div>

        <div>
          ${renderTerminal(scene.terminal, "distribution_playbook.log")}
        </div>
      </div>
    </section>
  `;
}

function renderSummary(scene) {
  const list = scene.points
    .map(
      (point, index) => `
      <article class="summary-item">
        <div class="summary-no">${String(index + 1).padStart(2, "0")}</div>
        <p>${escapeHtml(point)}</p>
      </article>
    `,
    )
    .join("");

  return `
    <section class="slide-shell summary-stage scene-enter">
      <div class="summary-shell">
        <h2 class="summary-title">${escapeHtml(scene.title)}</h2>
        <div class="summary-list">${list}</div>
        <div class="summary-actions">
          <button type="button" class="primary-cta" data-reset="true">↺ 从头再看一遍</button>
          <a class="ghost-cta" href="${repo}" target="_blank" rel="noreferrer">⭐ Star LivePPT</a>
          <a class="ghost-cta" href="${repo}/fork" target="_blank" rel="noreferrer">🍴 Fork 模板</a>
        </div>
      </div>
    </section>
  `;
}

function buildSlideMarkup(scene) {
  switch (scene.type) {
    case "cover":
      return renderCover(scene);
    case "pain":
      return renderPain(scene);
    case "split":
      return renderSplit(scene);
    case "simulator":
      return renderSimulator(scene);
    case "modules":
      return renderModules(scene);
    case "usecase":
      return renderUsecase(scene);
    case "summary":
      return renderSummary(scene);
    default:
      return `<section class="slide-shell scene-enter"><p>Unknown scene type.</p></section>`;
  }
}

function renderDots() {
  dotNav.innerHTML = slides
    .map(
      (scene, index) => `
      <button
        type="button"
        data-index="${index}"
        class="${index === current ? "is-active" : ""}"
        aria-label="第 ${index + 1} 页：${escapeHtml(scene.nav)}"
      ></button>
    `,
    )
    .join("");
}

function renderButtons() {
  prevBtn.disabled = current === 0;
  nextBtn.disabled = current === slides.length - 1;
}

function renderProgress() {
  const percent = ((current + 1) / slides.length) * 100;
  progressBar.style.width = `${percent}%`;
}

function renderStepHint() {
  const scene = slides[current];
  const prefix = `${String(current + 1).padStart(2, "0")} / ${String(slides.length).padStart(2, "0")}`;
  stepHint.textContent = `${prefix} · ${scene.nav}`;
}

function renderFooterScript() {
  scriptFooter.textContent = slides[current].script;
}

function renderSlide() {
  const scene = slides[current];
  slideRoot.innerHTML = buildSlideMarkup(scene);

  if (scene.type === "simulator") {
    patchSimulatorLogs();
  }

  renderDots();
  renderButtons();
  renderProgress();
  renderStepHint();
  renderFooterScript();
}

function stopAutoPlay() {
  if (!autoTimer) return;
  clearInterval(autoTimer);
  autoTimer = null;
  playBtn.classList.remove("is-playing");
  playBtn.textContent = "▶ 自动播放";
}

function startAutoPlay() {
  if (autoTimer) return;
  playBtn.classList.add("is-playing");
  playBtn.textContent = "⏸ 暂停自动播放";

  autoTimer = setInterval(() => {
    if (current >= slides.length - 1) {
      stopAutoPlay();
      return;
    }

    current += 1;
    renderSlide();
  }, 5600);
}

function goNextManual() {
  stopAutoPlay();
  if (current < slides.length - 1) {
    current += 1;
    renderSlide();
  }
}

function goPrevManual() {
  stopAutoPlay();
  if (current > 0) {
    current -= 1;
    renderSlide();
  }
}

function clearSimulatorTimers() {
  simulatorState.timers.forEach((timer) => clearTimeout(timer));
  simulatorState.timers = [];
}

function pushLogWithDelay(payload) {
  const timer = setTimeout(() => {
    simulatorState.logs.push({ text: payload.text, type: payload.type ?? "muted" });

    if (payload.done) {
      simulatorState.installed.add(payload.templateId);
      simulatorState.installing = null;
    }

    if (slides[current].type === "simulator") {
      renderSlide();
    }
  }, payload.delay);

  simulatorState.timers.push(timer);
}

function installTemplate(templateId) {
  const scene = slides.find((item) => item.type === "simulator");
  if (!scene) return;

  const template = scene.templates.find((item) => item.id === templateId);
  if (!template) return;

  if (simulatorState.installing || simulatorState.installed.has(templateId)) {
    return;
  }

  clearSimulatorTimers();

  simulatorState.installing = templateId;
  simulatorState.logs = [];

  if (slides[current].type === "simulator") {
    renderSlide();
  }

  const queue = [
    { delay: 200, text: `$ ${template.command}`, type: "cmd" },
    ...SIMULATOR_INSTALL_STEPS.map((step) => ({
      ...step,
      text: step.text.replace("{templateName}", template.name),
      templateId: step.done ? templateId : undefined,
    })),
  ];

  queue.forEach((step) => pushLogWithDelay(step));
}

function handleSlideClick(event) {
  const installButton = event.target.closest("[data-template-id]");
  if (installButton) {
    event.preventDefault();
    installTemplate(installButton.dataset.templateId);
    return;
  }

  const resetButton = event.target.closest("[data-reset='true']");
  if (resetButton) {
    event.preventDefault();
    stopAutoPlay();
    current = 0;
    renderSlide();
    return;
  }

  if (event.target.closest("a, button, [data-no-advance='true']")) {
    return;
  }

  goNextManual();
}

prevBtn.addEventListener("click", goPrevManual);
nextBtn.addEventListener("click", goNextManual);

playBtn.addEventListener("click", () => {
  if (autoTimer) {
    stopAutoPlay();
  } else {
    startAutoPlay();
  }
});

dotNav.addEventListener("click", (event) => {
  const dot = event.target.closest("button[data-index]");
  if (!dot) return;

  const index = Number(dot.dataset.index);
  if (Number.isNaN(index)) return;

  stopAutoPlay();
  current = Math.max(0, Math.min(index, slides.length - 1));
  renderSlide();
});

slideRoot.addEventListener("click", handleSlideClick);

document.addEventListener("keydown", (event) => {
  const activeTag = document.activeElement?.tagName;
  if (["INPUT", "TEXTAREA", "SELECT"].includes(activeTag)) return;

  if (event.key === "ArrowRight" || event.key === " ") {
    event.preventDefault();
    goNextManual();
    return;
  }

  if (event.key === "ArrowLeft") {
    event.preventDefault();
    goPrevManual();
    return;
  }

  if (event.key === "Home") {
    stopAutoPlay();
    current = 0;
    renderSlide();
    return;
  }

  if (event.key === "End") {
    stopAutoPlay();
    current = slides.length - 1;
    renderSlide();
  }
});

app.addEventListener("mousemove", (event) => {
  const bounds = app.getBoundingClientRect();
  const x = ((event.clientX - bounds.left) / bounds.width) * 100;
  const y = ((event.clientY - bounds.top) / bounds.height) * 100;
  app.style.setProperty("--mx", `${x.toFixed(2)}%`);
  app.style.setProperty("--my", `${y.toFixed(2)}%`);
});

window.addEventListener("beforeunload", () => {
  clearSimulatorTimers();
  stopAutoPlay();
});

renderSlide();
