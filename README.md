# 轻一点 · Lighter 官方网站

中英文官网、技术支持与隐私政策。使用 GitHub Pages 发布，纯静态 HTML / CSS / JavaScript，不依赖 npm、外部字体、第三方分析或 Cookie。

| 页面 | 简体中文 | English |
| --- | --- | --- |
| 官方网站 | https://weizhichao1027-collab.github.io/lighter-official/ | https://weizhichao1027-collab.github.io/lighter-official/en/ |
| 技术支持 | https://weizhichao1027-collab.github.io/lighter-official/support/ | https://weizhichao1027-collab.github.io/lighter-official/en/support/ |
| 隐私政策 | https://weizhichao1027-collab.github.io/lighter-official/privacy/ | https://weizhichao1027-collab.github.io/lighter-official/en/privacy/ |

支持邮箱：weizhichao1027@gmail.com。App 当前为 0.1.0 开发验证版本；无下载链接。官网上线与 App 发布分别管理。

## 本地构建和预览

需要 Python 3.10 或以上；生成网站只使用标准库。

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 4173 --directory site
```

打开 http://localhost:4173/。生成产物位于 `site/`，不提交 Git。GitHub Actions 会在 main 分支更新后构建、校验并部署。

## 内容维护

- `config.json`：支持邮箱、站点与仓库 URL、隐私政策日期、App 版本和 App Store 链接。
- `scripts/content.py`：中英文完整隐私政策和 12 个常见问题。
- `scripts/build.py`：语义化页面模板、官网文案、导航和 SEO 元数据。
- `assets/style.css`：紫罗兰 / 奶白 / 青柠视觉系统、响应式布局、键盘焦点、减少动态效果和打印样式。
- `assets/site.js`：手机导航、App 界面切换、FAQ 搜索与复制模板；无需联网、Cookie 或持久化浏览器存储。
- `assets/*.webp`：当前 App 真实开发截图与项目素材，截图只使用测试 / 示例资料。
- `scripts/check.py`：检查内部链接、锚点、资源、语言、页面元数据与基本隐私约束。

2026-10-05 图标已统一为用户选定的 26「双 L 精修」。导航与页脚的 `mark.svg` 嵌入由正式 AppIcon 导出的 `app-icon.png`，浏览器 PNG 图标与 Apple touch icon 也从同一正式图导出；分享卡左上标志已同步。`assets/icon-manifest.json` 记录选定源图与导出校验值。相关资源 URL 带内容版本参数，防止发布后继续显示旧缓存。2026-10-06 已推送 main，由 Pages 工作流构建发布。

正式上架后填写 `app_store_url`，并同步更新首页发布说明、支持 FAQ 和政策中的版本范围。所有公开措辞应与最终 App 的实际处理一致。未来启用账号、云端 AI、HealthKit、支付或分析功能时，先更新隐私说明，不能仅添加下载按钮。

## 隐私文案的实现依据

根据当前 iOS 工程的 SettingsView、LanguageSettings、LocalJSONStore、PrivacyInfo.xcprivacy 和 Info.plist 核对：本机记录；健康文件保护及排除备份；语言偏好独立保存；通知自愿启用；JSON 导出与外部副本；全部删除核验；当前无账号、后台服务、云端上传、第三方分析、广告、HealthKit 或订阅。

网站明确披露 GitHub Pages 为安全目的记录访客 IP，支持邮件属于主动提供信息。开发者无法远程访问本机记录。当前没有 JSON 导入或云端恢复功能。

资料参考：[GitHub Pages 数据收集](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection)、[GitHub 隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)、[Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)。本站文案不代表法律或医疗审签。

## 发布与回滚

Pages 源设为 GitHub Actions；`.github/workflows/pages.yml` 仅上传 `site/` 产物。主分支推送会自动部署。恢复到已验证的历史内容可用 `git revert <commit>` 后推送；不要以强制推送覆盖历史政策。

本仓库只包含公开网站，原生 App 源码、用户数据、证书、私钥与开发日志不上传。
