# Institute for Digital Consciousness

The website source for the Institute for Digital Consciousness, an independent research institute pursuing analysis on the ethical implications of advanced AI systems.

Built with [Hugo](https://gohugo.io/) and the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. Deployed on Netlify. Content managed via [Decap CMS](https://decapcms.org/).

## Site

The live site is at [digitalconsciousness.institute](https://digitalconsciousness.institute).

## Structure

- `content/` — Site content (Markdown files)
  - `working-papers/` — Working Papers series
  - `research.md`, `about.md`, `the-puppet-condition.md` — Top-level pages
- `assets/css/extended/custom.css` — Custom theme styling
- `static/admin/` — Decap CMS admin panel
- `layouts/` — Hugo template overrides
- `hugo.yaml` — Hugo configuration
- `netlify.toml` — Netlify build configuration

The PaperMod theme is fetched during build via `netlify.toml`; it is not committed to this repository.

## License

Site source: MIT.
Content (text, written work): © Bahadır Arıcı, all rights reserved unless otherwise noted.
