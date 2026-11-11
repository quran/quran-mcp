# Plugin artwork

These files are copied from the canonical brand exports. The portable manifest
references `listing-navy.png` as `logo` for light appearance,
`icon.png` as `logoDark` for dark appearance, and
`composer-96.png` as `composerIcon` inside `extensions.com.openai.interface`.
The package builder includes the artwork and verifies every referenced path.
The server's sidebar entrypoint uses the separate monochrome sidebar symbol.

| File | Covers | Purpose |
|---|---|---|
| `listing-navy.svg` | Light-appearance listing vector | Square vector navy rhombus with cyan artwork and transparent exterior. |
| `listing-navy.png` | Plugin listing in light appearance | Approved 512px navy rhombus with cyan artwork and transparent exterior. |
| `icon-light.png` | Light host appearance | 512px black rhombus with white artwork. |
| `icon-light.svg` | Light host appearance | Vector rendition of the same black/white symbol. |
| `icon-dark.png` | Dark host appearance | 512px white rhombus with dark artwork. |
| `icon-dark.svg` | White-rhombus variant and study skill source | Vector rendition of the same white/dark symbol. |
| `icon.png` | Plugin listing in dark appearance and fallback | 512px cyan rhombus with navy artwork. |
| `icon.svg` | Dark-appearance listing vector and fallback | Vector rendition of the cyan/navy symbol. |
| `composer-48.png` | Composer and single-image extension slots | 48px mint/navy symbol. |
| `composer-96.png` | Composer at higher pixel density | 96px mint/navy symbol. |
| `server-128.png` | Small server identity | 128px mint/navy symbol. |
| `server-512.png` | Large server identity | 512px mint/navy symbol. |
| `sidebar-icon.svg` | Theme-inheriting calligraphy rendition | 20px transparent foreground artwork using `currentColor`, without the enclosing rhombus. |
| `sidebar-icon-light.svg` | Reader entrypoints in light appearance | 20px black calligraphy on a transparent background. |
| `sidebar-icon-dark.svg` | Reader entrypoints in dark appearance | 20px white calligraphy on a transparent background. |
