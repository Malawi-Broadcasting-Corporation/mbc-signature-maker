# MBC Email Signature Maker

A one-page tool for MBC staff to create their branded email signature.
Type your details, preview the signature live, and download it as a high-resolution PNG.

## Using it

1. Open the published page (GitHub Pages) or open `index.html` directly in Chrome or Edge.
2. Fill in your name, job title, phone and email.
3. Choose an image size and click **Download PNG**, or **Copy image** to paste straight into Outlook or Gmail.

Leave a field empty to hide that line. Long names and titles shrink automatically to fit.

### Social media icons

Icons use MBC Maroon `#941C26` (Pantone 7427 C).

The official Instagram, X and Facebook icons are built in when their files are in `source/assets/social/`
(`instagram.svg`/`.png`, `x.svg`/`.png`, `facebook.svg`/`.png`) at build time. Without a file, that platform shows a maroon
letter badge (IG, X, FB). Staff can also load a replacement icon in the **Social media icons** section; it is remembered
in that browser on that computer.

## Project layout

| Path | Purpose |
| --- | --- |
| `index.html` | The finished, self-contained tool (fonts and logos embedded). This is what GitHub Pages serves. |
| `source/template.html` | Editable source of the page. |
| `source/assets/` | MBC logo and sub-brand logos and the brand swirl watermark (from the 2024 MBC Branding and Marking Guidelines). |
| `source/fonts/` | Montserrat (SIL Open Font License, see `OFL-LICENSE.txt`). |
| `source/build.py` | Rebuilds `index.html` from the template, assets and fonts. |

## Making changes

Edit `source/template.html` (or replace files in `source/assets/`), then run:

```bash
python source/build.py
```

Commit both the source change and the regenerated `index.html`.

## Publishing with GitHub Pages

Repository **Settings → Pages → Build and deployment**: Source **Deploy from a branch**, branch **main**, folder **/ (root)**.
The site will be available at `https://<organisation>.github.io/mbc-signature-maker/`.

## Brand reference

Colours follow the MBC Brand Guidelines 2024: Maroon `#941C26`, Red `#DE232A`, Green `#02964E`, Black `#000000`.
Primary typeface: Montserrat.
