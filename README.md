# EG-based-characterization-of-auditory-attention-and-meditation

Exploratory EEG preprocessing and ERP analysis inspired by [the paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12417730/).

## Notebooks

Run these in order, with Jupyter started in this repository folder:

1. **eeg exploration.ipynb** loads subject 001, run 1 from OpenNeuro ds003061, sets channel information and the BioSemi 64 montage, applies an average reference and a 1 Hz high-pass filter, fits 20 ICA components, and provides plots for artifact inspection. The last cell saves `sub-001_run-1_clean_raw.fif`.
2. **analyisis.ipynb** loads that cleaned recording, creates epochs from -0.2 to 0.8 seconds with a -0.2 to 0 second baseline, averages standard/oddball/noise trials, compares standard and oddball ERPs at Pz, and plots oddball scalp maps at 100, 200, 350, and 500 ms.

The analysis filename retains its original spelling.

## Setup

Python 3.10 was used for the local notebook work. Create and activate a virtual environment, then run:

```sh
python -m pip install -r requirements.txt
python -m jupyterlab
```

Select that environment as the notebook kernel. The notebooks also contain installation cells retained from the original workflow; these are optional after installing the requirements.

The first notebook downloads subject 001 if its `.set` file is missing. Keep both the EEGLAB `.set` file and any companion data files together. Raw data and the generated cleaned FIF file are not tracked in Git.

## Data and interpretation

Data: **EEG data from an auditory oddball task**, Arnaud Delorme, [OpenNeuro ds003061, snapshot 1.1.2](https://openneuro.org/datasets/ds003061/versions/1.1.2), DOI [10.18112/openneuro.ds003061.v1.1.2](https://doi.org/10.18112/openneuro.ds003061.v1.1.2).

- The `Temp` channel is treated as a miscellaneous channel rather than a scalp EEG electrode.
- ICA exclusions `[0, 4, 6]` are the current exploratory selection. Component numbering can change when ICA is fitted again; inspect the component plots and overlays before using those exclusions. The ICA fit currently has no fixed random seed.
- Response-tagged sound annotations are grouped with their sound condition, including the dataset spelling `reponse`.
- This is a single-subject, single-run exploration. It does not reproduce the paper's participant-level figures or its meditation classification results. The available task annotations do not label meditation versus cognitive states.

Notebook outputs are cleared in the uploaded copies. Original local notebooks and their saved outputs were preserved. File paths were made relative, and a final save cell was added to connect the two notebooks. Downloaded data, local package installations, and generated recordings are excluded.
