# Customizing Your MkDocs Site

## Theme Customization

### Colors and Fonts

You can customize the Material theme by modifying the `mkdocs.yml` file:

```yaml
theme:
  name: material
  palette:
    primary: indigo
    accent: indigo
  font:
    text: Roboto
    code: Roboto Mono
```

### Navigation

Configure the navigation structure:

```yaml
nav:
  - Home: index.md
  - User Guide:
    - Getting Started: guide/getting-started.md
    - Customization: guide/customization.md
```

## Adding Extensions

Enable Markdown extensions in `mkdocs.yml`:

```yaml
markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
```

## Custom CSS

Create a `docs/stylesheets/extra.css` file:

```css
:root {
  --md-primary-fg-color: #007bff;
}
```

Then add it to `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
```
