# MBC Email Signature Maker

A one-page tool for MBC staff to create their branded email signature.
Type your details, preview the signature live, and download it as a high-resolution PNG.

## Using it

1. Open the published page (GitHub Pages) or open `index.html` directly in Chrome or Edge.
2. Fill in your name, job title, phone and email.
3. Choose an image size and click **Download PNG**, or **Copy image** to paste straight into Outlook or Gmail.

Leave a field empty to hide that line. Long names and titles shrink automatically to fit.
Staff with a second phone number or email can add it in the optional **Second phone** / **Second email** fields;
it appears on the same line as the first, separated by a divider.

### Social media icons

By default Instagram, X and Facebook show red letter badges (IG, X, FB).
To use the official platform icons, download them from each platform's brand resources and load them in the
**Social media icons** section. They are remembered in that browser on that computer.

## Project layout

| Path | Purpose |
| --- | --- |
| `index.html` | The finished, self-contained tool (fonts and logos embedded). This is what GitHub Pages serves. |
| `source/template.html` | Editable source of the page. |
| `source/assets/` | MBC logo and sub-brand logos (extracted from the MBC Brand Guidelines 2024). |
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
