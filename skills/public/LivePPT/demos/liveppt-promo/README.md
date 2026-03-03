# LivePPT Promo Demo

这是一个基于 LivePPT Skill 的“项目推广动态PPT”示例，用于推广：
`https://github.com/AIPMAndy/LivePPT`

当前视觉已升级为白色奢侈品风（Ivory Luxe），不再使用苹果系浅色玻璃卡片语言。

## Files

- `index.html`：主页面（可点击/键盘切屏）
- `styles.css`：主题与布局
- `script.js`：分镜数据与交互逻辑
- `scene-map.md`：逐屏叙事大纲
- `theme-spec.md`：主题令牌定义
- `plan-7d.md`：由脚本生成的 7 天执行计划

## Run

方式一（直接双击）：

- 打开 `index.html`

方式二（本地服务，推荐）：

```bash
cd skills/public/LivePPT/demos/liveppt-promo
python3 -m http.server 4188
```

然后访问：`http://localhost:4188`

## Controls

- `←` / `→`：上一页 / 下一页
- `Home` / `End`：跳到首尾页
- `自动播放`：每 5.6 秒自动切屏
