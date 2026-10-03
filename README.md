# Academic NLP Text Classification Prototype

This repository contains coursework exploring text preprocessing, TF-IDF features, and classical machine-learning classifiers.

## Important limitation

An earlier version of this project described the task as **mental-health-status classification** and mapped general sentiment labels to terms such as “normal” and “depression”. That mapping is **not clinically valid**: sentiment in a movie review or general text cannot be used to infer a person's mental-health condition.

Accordingly, this repository should be treated as an **academic NLP prototype**, not as a diagnostic system or a validated mental-health prediction tool.

## What is technically demonstrated

- Text cleaning and tokenization
- Stop-word removal
- TF-IDF vectorization
- Linear SVM / Logistic Regression experiments
- Train/test evaluation
- Model serialization
- A simple Streamlit interface

## Repository Contents

- `Mental_health_status_classification.ipynb` — early experimental notebook
- `Model_training.ipynb` — feature extraction and model training
- `src/app.py` — Streamlit prototype
- `models/` — saved model/vectorizer artefacts
- `requirements.txt`

## Recommended next step

For a defensible portfolio project, this pipeline should be retrained on a dataset whose labels directly match the stated prediction task—for example, a standard sentiment-analysis dataset if the goal is sentiment classification.

## Responsible-use note

Outputs from the existing model must not be interpreted as medical diagnoses, screening results, or assessments of a person's mental-health status.
