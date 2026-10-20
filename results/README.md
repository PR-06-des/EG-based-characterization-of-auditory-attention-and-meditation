# Saved analysis results

These compact exports come from the executed `figure replications.ipynb` using hu-neuro-pipeline 0.9.0 on OpenNeuro ds003061, snapshot 1.1.2. The original participant/run files and full processing derivatives remain local.

- `figures/`: 11 group-level PNG figures, including ERP waveforms, scalp maps and PSD.
- `paper_comparison/`: 14 group-level PNG figures plus numerical traces, calibration, grand-waveform peak/scale differences, spatial power values and figure-by-figure reproduction status.
- `grand_average_peaks.csv`: grand-waveform peak measurements.
- `mean_eeg_power.csv`: group PSD values in microvolt squared/Hz and dB relative to 1 microvolt squared/Hz.
- `analysis_settings.json`, `software_versions.json`, `run_summary.json`: processing settings, executed environment and run totals.

Participant-level peak/retention reports, the per-recording inventory, individual participant plots and plot-position mappings remain local. The source notebook generates those outputs for local inspection; they are excluded from this published result bundle.

The run covers 13 participants and 39 recordings: 28,452 sound events, 27 excluded recording-edge windows, 28,425 epoched trials and 25,550 retained trials. Standard, oddball and noise sounds are kept distinct. Runs are pooled within participants; participants contribute equally to grand averages.

Paper comparison values remain on their measured scales. The locally generated first-five-subject panel is a layout demonstration, since the article does not identify its P1-P5 mapping. Digitized reference curves are approximate image measurements, with pixel envelopes saved separately. Spectral normalization in the publication is unspecified, so the scale comparison is not a unit-harmonized statistical test.

Recreate all figures by running the notebook after downloading the dataset. Full FIF derivatives, intermediate caches and PDF exports are generated under `hu_neuro_results/`, which is excluded from Git.
