# 🔐 Effectiveness and Adaptability of Open-Source Anonymization Tools

This repository contains the data generation engine and experimental configuration files used in the Master's dissertation project at **Transilvania University of Brașov (UNITBV)**.

The project focuses on evaluating anonymization techniques and tools such as ARX and sdcMicro using synthetic datasets that simulate realistic university administrative data while ensuring full GDPR compliance.

---

## 📊 1. Dataset Generation

The script `dataset_generator.py` generates a synthetic dataset of **10,000 records**, designed to mimic a university administrative database.

The dataset is fully artificial and does not contain any real personal information.

### 🧾 Data Structure

**Direct Identifiers:**
- Name  
- Student_ID  
- Email  

**Quasi-identifiers:**
- Date of Birth  
- Gender  
- Postal Code  
- Degree Program  
- Year of Study  

**Sensitive Attributes:**
- Medical Indicator (used for l-diversity and t-closeness experiments)

---

## ⚙️ 2. Installation & Reproducibility

To replicate the dataset generation process:

```bash
python dataset_generator.py
