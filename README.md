# Identification of Antigen-Specific T Cell Receptors with Combinatorial Peptide Pooling

Supplementary repository to the paper: [bioRxiv version](https://www.biorxiv.org/content/10.1101/2023.11.28.569052v1).

T cell receptor (TCR) repertoire diversity enables the antigen-specific immune responses against the vast space of possible pathogens. Identifying TCR-antigen binding pairs from the large TCR repertoire and antigen space is crucial for biomedical research.  Here, we introduce *copepodTCR*, an open-access tool to design and interpret high-throughput experimental TCR specificity assays. *copepodTCR* implements a combinatorial peptide pooling scheme for efficient experimental testing of T cell responses against large overlapping peptide libraries, that can be used to identify the specificity of (or "deorphanize") TCRs. The scheme detects experimental errors and, coupled with a hierarchical Bayesian model for unbiased interpretation, identifies the response-eliciting peptide sequence for a TCR of interest out of hundreds of peptides tested using a simple experimental set-up. Using *in silico* simulations, we demonstrate the varied experimental settings in which *copepodTCR* yields efficient and interpretable TCR specificity results. We validated our approach on a library of 253 overlapping peptides covering the SARS-CoV-2 spike protein, split across 12 pools. A single stimulation with combinatorial pools identified the correct epitope of two TCRs with known specificity and then deorphanized two SARS-CoV-2 associated TCRs shared among a large cohort of COVID-19 patients. 
We provide experimental guides to efficiently design larger screens covering thousands of peptides which will be crucial to identify antigen-specific T cells and their targets from limited clinical material.

### Figures

- Figures1-2-3.ipynb contains the code for figures in the main part of the manuscript. The data used in them is in "data" folder.
- Figures_Extended-data.ipynb contains the code for Extended data figures.
- Figures-Supplement.ipynb contains the code for figures from the supplementary materials.

In the code, we use *codePUB* and *copepodTCR* python packages. *codePUB* is installed automatically when you install *copepodTCR*:

```python
pip install copepodTCR
```

or with conda:

```python
conda install -c vasilisa.kovaleva copepodTCR
```

*copepodTCR* documentation: [readthedocs](https://copepodTCR.readthedocs.io/en/latest/Introduction.html).

### In silico simulations

Code for *in silico simulations* is in separate repository: [Peptide pooling simulation](https://github.com/meyer-lab-cshl/peptide_pooling_simulation)

### Authors

Vasilisa A. Kovaleva, David J. Pattinson, Guanchen He, Carl Barton, Sarah R. Chapin, Anastasia A. Minervina, Qin Huang, Paul G. Thomas, Mikhail V. Pogorelyy, Hannah V. Meyer