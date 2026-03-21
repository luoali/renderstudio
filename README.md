# RenderStudio

A Gemini-powered image generation workbench. Direct API access, no middleman, data stays in your browser.

**Try it** → [renderstudio.pages.dev](https://renderstudio.pages.dev)

## Features

- **Timeline-based iteration** — Every round is saved with its prompt. Jump back to any previous version and branch from there
- **Image annotation** — Draw directly on the image to mark exactly what needs to change. Freehand, rectangles, arrows, text
- **Privacy first** — API Key and generated images never leave your browser. Stored locally in IndexedDB
- **No watermark** — Direct API call, clean output
- **Cost tracking** — Estimated cost shown after each generation (actual billing via Google)
- **Backup & restore** — Export all history and generated images as a zip. Import on any device

## Models

| Name | API |
|------|-----|
| Nano Banana Pro | `gemini-3-pro-image-preview` |
| Nano Banana 2 | `gemini-3.1-flash-image-preview` |

## Usage

Open [renderstudio.pages.dev](https://renderstudio.pages.dev) and enter your [Google AI Studio API Key](https://aistudio.google.com/apikey).

## Run locally

```bash
git clone https://github.com/luoali/renderstudio
cd renderstudio
pip install flask flask-cors requests
python app.py
# Open http://localhost:8080
```

## Self-hosting

Fork this repo, connect to Cloudflare Pages, deploy `index.html` directly. No build step needed.

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — Attribution, non-commercial use only

---

# RenderStudio（中文说明）

直连 Gemini 官方 API 的图片生成工作台。自备 Key，数据只在你的浏览器。

**在线使用** → [renderstudio.pages.dev](https://renderstudio.pages.dev)

## 特点

- **时间轴与迭代控制** — 每轮图和描述词都记录在时间轴，可重做这轮，或从任意历史轮次继续生成
- **内置标注画板** — 直接在图上画圈、框选、写箭头，精准告诉模型改哪里
- **极致隐私保护** — API Key 不上传，图片不上传，全部存在本地浏览器的 IndexedDB
- **高画质，无水印** — 直连官方 API，输出无平台水印，分辨率可选
- **费用透明** — 每次生成实时显示预估费用，实际以 Google 账单为准
- **本地数据导出与备份** — 一键导出全部历史画板及所有生成图片，换设备直接导入

## 本地运行

```bash
git clone https://github.com/luoali/renderstudio
cd renderstudio
pip install flask flask-cors requests
python app.py
# 打开 http://localhost:8080
```

## 网页版部署

Fork 本仓库，在 Cloudflare Pages 连接 repo，直接部署 `index.html`，无需构建步骤。

## 获取 API Key

访问 [Google AI Studio](https://aistudio.google.com/apikey)，需绑定银行卡开通付费后即可使用。

## 许可

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) · 署名 · 非商业使用
