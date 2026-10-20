# Published figure references

The eleven `figure_*.jpg` files are unchanged published images from:

Attar ET (2025). *EEG-based characterization of auditory attention and meditation: an ERP and machine learning approach*. Frontiers in Human Neuroscience 19:1616456. [DOI](https://doi.org/10.3389/fnhum.2025.1616456), [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12417730/).

They are reproduced under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). Copyright 2025 Attar. `sources.json` records the original asset URLs, dimensions and SHA-256 hashes. These files are reference assets, not recomputed results.

The notebook attributes references separately from its own data-derived panels. Figures 8-11 are labeled simulations in the publication. Approximate digitized traces, calibration and comparison figures are under `results/paper_comparison/`.

To restore missing reference images from the source manifest:

```sh
python paper_references/download_references.py
```

The local cached article HTML is excluded from version control.
