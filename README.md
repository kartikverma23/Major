# Pneumonia Detection from Chest X-ray Images

A machine-learning project for classifying chest X-ray images into **NORMAL** and **PNEUMONIA** classes. The repository contains the original project notebooks, repaired historical workflows, and a clean reproducibility layer for local and Google Colab runs.

> **Important:** This is an educational computer-vision project, not a clinical diagnostic tool. It must not be used for medical decisions.

## Project context

This repository preserves work associated with the 2022–23 project and the paper *Application of CNN Model on Medical Image*. The paper and notebook outputs contain historical results, including comparisons across CNN/transfer-learning approaches. Those historical numbers should be treated as reported project results; they are not represented here as a fresh independent clinical validation.

## What was repaired

- Replaced Kaggle-only `../input/...` paths in `1.ipynb` and `2.ipynb` with the repository's local dataset path.
- Corrected the dataset path in `test.ipynb`.
- Added `requirements.txt` for a reproducible Python environment.
- Added `scripts/validate_dataset.py` as a lightweight preflight check.
- Added this README with setup, limitations, and a clear run order.
- Added `notebooks/colab_pneumonia_detection.ipynb`, a clean Colab workflow with class weights, modern TensorFlow APIs, test metrics, model export, and an optional Gradio demo.
- Repaired accidental notebook indentation errors, stale Kaggle paths, deprecated Keras imports, and deprecated Seaborn plotting calls in the retained notebooks.

The original notebooks and data are retained. The repository currently includes a large dataset; a future cleanup could move the dataset to an external download step to make cloning faster.

## Repository layout

```text
.
├── 1.ipynb                         # Historical CNN and transfer-learning experiments
├── 2.ipynb                         # Additional transfer-learning experiments
├── 3.ipynb                         # Custom CNN experiment
├── test.ipynb                      # Historical consolidated experiment notebook
├── notebooks/reproducible_cnn.ipynb # Clean output-stripped notebook
├── Dicom/Test_Images/              # DICOM test images
├── Dicom/test.py                   # DICOM-to-JPEG conversion utility
├── chest-xray-pneumonia/           # Dataset used by the notebooks
├── scripts/validate_dataset.py     # Dataset layout preflight
└── requirements.txt
```

## Run on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kartikverma23/Major/blob/main/notebooks/colab_pneumonia_detection.ipynb)

Open the badge above and run `notebooks/colab_pneumonia_detection.ipynb`. The notebook detects the repository dataset, trains a compact CNN, evaluates precision/recall/F1 and ROC-AUC, saves `artifacts/pneumonia_cnn.keras`, and can optionally launch a Gradio demo. Select a GPU runtime before training. The repository includes the image dataset, so the first Colab setup cell may take several minutes to clone.

## Run locally

Use Python 3.10 or 3.11. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/validate_dataset.py
jupyter notebook notebooks/reproducible_cnn.ipynb
```

Start with `notebooks/reproducible_cnn.ipynb` for the clean CNN workflow. The historical notebooks are retained for reference. The other notebooks contain additional model experiments and may download pretrained weights on first use. Training is resource-intensive and may require a GPU or substantial CPU time.

### DICOM conversion

To convert the sample DICOM files to JPEG:

```bash
python Dicom/test.py
```

The conversion utility is separate from the pneumonia-classification training workflow.

## Data and limitations

- The repository contains the chest X-ray dataset used by the project; check the dataset's original source and terms before redistribution.
- The dataset is imbalanced and the validation split is small, so accuracy alone is not sufficient to judge model quality.
- Results can be affected by preprocessing, augmentation, data leakage, class imbalance, and differences between training and real-world clinical images.
- No claim of clinical readiness or generalization is made.

## Recruiter-facing summary

This project demonstrates an end-to-end machine-learning workflow: dataset inspection, image preprocessing, augmentation, CNN and transfer-learning model comparison, evaluation with accuracy/precision/recall/F1 and confusion matrices, and DICOM-to-JPEG preprocessing. It is best discussed as an academic computer-vision project and as evidence of experience with Python, TensorFlow/Keras, OpenCV, pydicom, model evaluation, and reproducible experimentation.
