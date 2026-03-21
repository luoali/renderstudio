# RenderStudio

直连 Gemini 官方 API 的图片生成工作台。自备 Key，数据只在你的浏览器。

**在线使用** → [renderstudio.pages.dev](https://renderstudio.pages.dev)

## 特点

- **时间轴与迭代控制** — 每轮图和描述词都记录在时间轴，可重做这轮，或从任意历史轮次继续生成
- **极致隐私保护** — API Key 不上传，图片不上传，全部存在本地浏览器的 IndexedDB
- **内置标注画板** — 直接在图上画圈、框选、写箭头，精准告诉模型改哪里
- **高画质，无水印** — 直连官方 API，输出无平台水印，分辨率可选
- **费用透明** — 每次生成实时显示消耗费用
- **本地数据便携** — 一键导出全部历史画板，换电脑直接导入

## 使用

打开 [renderstudio.pages.dev](https://renderstudio.pages.dev)，填入 [Google AI Studio API Key](https://aistudio.google.com/apikey) 即可。

## 本地运行

```bash
git clone https://github.com/luoali/renderstudio
cd renderstudio
pip install flask flask-cors requests
python app.py
# 打开 http://localhost:8080
```

## 自行部署

Fork 本仓库，在 Cloudflare Pages 连接 repo，直接部署 `index.html`，无需构建步骤。

## 模型

| 模型 | API 名称 |
|------|---------|
| Nano Banana Pro | `gemini-3-pro-image-preview` |
| Nano Banana 2 | `gemini-3.1-flash-image-preview` |

## 许可

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) · 署名 · 非商业使用
