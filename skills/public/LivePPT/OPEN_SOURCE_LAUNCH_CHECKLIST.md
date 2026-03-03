# Open Source Launch Checklist

适用于 `LivePPT` 首次公开发布与后续版本发布。

## 1) Pre-Launch Validation

- [ ] 在 skill 根目录执行 `make validate` 并通过。
- [ ] 手动跑一次计划生成、主题生成、release note 生成命令。
- [ ] 确认 `README.md`、`SKILL.md`、`CONTRIBUTING.md` 与当前行为一致。

## 2) Repository Hygiene

- [ ] 确认 `LICENSE`、`ROADMAP.md`、`CHANGELOG.md` 已更新。
- [ ] 确认无敏感信息（token、密钥、账号凭据）被提交。
- [ ] 确认生成目录（如 `plans/`、`themes/`）不会进入版本库。

## 3) Release Preparation

- [ ] 生成或更新版本说明：`make release-note VERSION=<version>`。
- [ ] 在 `releases/<version>.md` 填写 Added/Changed/Fixed/User Value。
- [ ] 核对版本号、发布日期和 Roadmap 阶段是否一致。

## 4) Public Publishing

- [ ] 打 tag（如 `v0.1.2`）并发布 GitHub Release。
- [ ] 在 README 中补充 demo 链接（可选 GIF/截图）。
- [ ] 发布后 48 小时内处理首批 issue / PR 反馈。
