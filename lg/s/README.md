# Sofian Alqurashi — Email Signature

HTML email signature for **Larksuite / Lark Mail** (also works in Gmail, Outlook, Apple Mail).

## 📦 What's in this package

| File | Purpose |
|------|---------|
| `signature_base64.html` | Self-contained signature with images embedded as Base64 (~226 KB). No hosting required. |
| `signature_external.html` | Lightweight signature (~10 KB) referencing externally hosted images. |
| `slices/` | 19 PNG slices that make up the signature. Upload these to your CDN/host for the external version. |
| `preview.html` | Open in any browser to see the rendered signature with all click targets working. |

---

## 🚀 Quick start (Larksuite)

### Option A — Base64 version (easiest, no hosting)

1. Open `signature_base64.html` in a text editor
2. Select all (`Ctrl/Cmd + A`) → Copy
3. Larksuite → Settings → Mail → Signature → switch editor to **HTML / Source mode**
4. Paste → Save

### Option B — External URL version (lightweight, recommended for daily use)

1. Upload all 19 files from `/slices` to your web host (e.g. `https://yourdomain.com/sig/`)
2. Open `signature_external.html`
3. Find & replace `https://YOUR-HOST.com/sig/` → your actual URL
4. Paste into Larksuite signature (HTML mode) → Save

---

## 🔗 Clickable regions (19 slices, 16 are linked)

| # | Region | Action |
|---|--------|--------|
| 01 | QR code area | Opens website |
| 02 | Legend Group main logo | Opens website |
| 03 | Legend Digital logo | `legendgroup.sa/digital` |
| 04 | Legend Events logo | `legendgroup.sa/events` |
| 05 | Legend Equipped logo | `legendgroup.sa/equipped` |
| 06 | Legend Expo logo | `legendgroup.sa/expo` |
| 07 | Decorative top bar | _(not linked)_ |
| 08 | Name + Title | Opens website |
| 09 | Phone number | `tel:+966543663939` |
| 10 | Email address | `mailto:s.alqurashi@legendgroup.sa` |
| 11 | Website | `https://www.legendgroup.sa` |
| 12 | King Road - Jeddah | Google Maps |
| 13 | An-Narjis - Riyadh | Google Maps |
| 14 | Dark left padding | _(not linked)_ |
| 15 | TikTok icon | `tiktok.com/@legendgroup` ⚠️ verify handle |
| 16 | LinkedIn icon | `linkedin.com/company/legendgroup` ⚠️ verify handle |
| 17 | Instagram icon | `instagram.com/legendgroup` ⚠️ verify handle |
| 18 | X (Twitter) icon | `x.com/legendgroup` ⚠️ verify handle |
| 19 | Dark right padding | _(not linked)_ |

⚠️ **Action required:** Verify the social media URLs (15–18) match your actual handles. If they differ, search for the placeholder URL in the HTML and replace it.

---

## ⚠️ Notes

- **Larksuite**: confirmed working, supports HTML signatures with images and links
- **Gmail**: copying from `preview.html` rendered in a browser → "Copy" → paste into Gmail signature usually works better than pasting raw HTML (Gmail strips some tags)
- **Outlook desktop**: prefers the external URL version; Base64 may be downsized
- **Image dimensions**: 800×356 px total. Don't resize in the email client — it will blur the slices
