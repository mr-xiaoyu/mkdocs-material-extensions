# Material for MkDocs Extensions

This project provides extensions for the documentation template
[Material for MkDocs][1].

## Version selection

To generate a version selection dropdown next to the title in the header,
provide a JSON file with the following structure:

```json
{
  "versions": [
    {
      "name": "LATEST",
      "url": "https://plossys-5.docs.sealsystems.de"
    },
    {
      "name": "5.1.5.6382",
      "url": "https://v5.1.5.6382.plossys-5.docs.sealsystems.de"
    },
    {
      "name": "5.0.1.4245",
      "url": "https://v5.0.1.4245.plossys-5.docs.sealsystems.de"
    }
  ],
  "warning": "..."
}
```

This JSON file can then be transformed using the `version.py` script (in the
root folder) to generate the `overrides/partials/version.html` partial
containing the actual version selection, e.g.:

``` sh
./version.py data/version.json
```

This partial is then included in the `header.html` partial. The version which is
listed __first__ in the JSON file is assumed to be the latest version and will
render first. The selected version is determined by comparing each version `url`
against the `site_url` in the `mkdocs.yml` file. If the selected version is not
the first, a warning icon with a tooltop is rendered next to the dropdown. The
tooltip text can be changed by adjusting the `warning` key in the JSON file.

  [1]: https://squidfunk.github.io/mkdocs-material/