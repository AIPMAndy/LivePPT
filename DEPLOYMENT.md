# LivePPT 官网部署与验收

LivePPT 官网是仓库根目录的 \`index.html\`。它通过相对路径嵌入 \`skills/public/LivePPT/demos/liveppt-promo/index.html\` 真实演示，无需 npm、后端和第三方构建服务。

## 首次启用 GitHub Pages

1. 将优化 PR 合并到 \`main\`。
2. 打开仓库 **Settings → Pages**。
3. 在 **Build and deployment → Source** 选择 **Deploy from a branch**。
4. Branch 选 **main**，文件夹选 **/(root)**，点击 **Save**。
5. 等待 GitHub 的 Pages 部署完成，在 **Settings → Pages → Visit site** 取得实际访问地址。

标准项目地址通常是：

\`\`\`text
https://aipmandy.github.io/LivePPT/
\`\`\`

> URL 只有 Pages 成功启用、构建后才有效，不应把预期地址当作已上线证明。无需配置自定义域名。

官方文档：[Configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 本地预览

从仓库根目录运行：

\`\`\`bash
python3 -m http.server 8000
\`\`\`

打开 \`http://localhost:8000/\`。首页内嵌实际 demo；可用「全屏打开」在独立页面检查交互。

## 发布验收清单

- [ ] 首页 HTTP 200，标题、导航和三项快速开始信息可见
- [ ] 「在线体验」能跳转到 Demo，嵌入窗口正常
- [ ] 全屏 Demo 可翻页、键盘操作并可暂停自动播放
- [ ] 「复制命令」在 HTTPS 下正确复制；失败时有反馈
- [ ] iPhone/Android 窄屏没有横向溢出，文字可阅读
- [ ] 外链带 HTTPS 且指向正确项目，不包含测试域名
- [ ] 根目录 GitHub Actions \`Validate LivePPT\` 检查为绿色
- [ ] 生成器回归测试通过；包含脚本注入样本
- [ ] 授权冲突已由仓库负责人确认后再广泛商业分发

## 排障

- **404**：检查 Pages 是否启用及发布源是否为 \`main /(root)\`，并确认 PR 已合并。
- **页面可打开但 Demo 无法展示**：检查相对路径是否完整保留，并直接打开子目录里的 \`index.html\`。
- **改动没有更新**：查看仓库 Actions 的 Pages 部署结果；不要依赖浏览器本地缓存判断是否发布成功。
- **本地 \`file://\` 复制失败**：使用本地 HTTP 服务或部署到 HTTPS Pages 环境。

## 维护原则

首页预览和 Python 输出是两条入口：官网主要展示仓库中的交互演示；命令行脚本生成的是用户自己的单文件 HTML。发布文案应如实区分两种能力，避免宣称已经支持 PPTX 导出、任意复杂布局保真、在线协作编辑或 AI 云端生成。
