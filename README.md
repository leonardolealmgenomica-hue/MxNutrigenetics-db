# Mexican Genome Nutrigenetics SNP Database

A curated database of Single Nucleotide Polymorphisms (SNPs) specifically relevant to the Mexican population, focusing on nutrigenetics, metabolic health, and disease prevention.

## Project Overview
This project implements the **Mexican Genome model**, a precision nutrition framework tailored to the genetic background of the Mexican population. It provides a structured database of variants that influence how individuals respond to diet, specifically addressing prevalent health challenges in Mexico like MASLD (Metabolic Dysfunction-Associated Steatotic Liver Disease), Type 2 Diabetes, and Dyslipidemia.

## Key Features
- **Mexican-Specific Data:** Includes Minor Allele Frequencies (MAF) specifically for the Mexican population (MXL 1000 Genomes).
- **Comprehensive Variant Mapping:** 14 high-evidence SNPs across 6 metabolic areas:
    1. Carbohydrate Metabolism (TCF7L2, PPARG, KCNJ11)
    2. Lipid Metabolism (APOE, FADS1, APOA5)
    3. Inflammatory Response (TNF, IL6)
    4. Micronutrient Metabolism (MTHFR, VDR, HFE)
    5. MASLD / Liver Disease Risk (PNPLA3, TM6SF2)
    6. Food Intolerances (MCM6/LCT, CYP1A2)
- **Clinical & Nutritional Insights:** Each entry provides functional effects, evidence levels (A/B/C), and personalized dietary recommendations.
- **Cultural Relevance:** Suggestions include traditional Mexican foods (Nopal, Amaranth, Chia, Quelites) to improve dietary adherence.

## Database Structure
Each SNP entry contains:
- `rs_id`: dbSNP identifier.
- `maf_mexican`: Local frequency data.
- `effect`: Molecular and physiological impact.
- `nutrients_up/down`: Specific nutritional interventions.
- `foods_recommended/avoid`: Culturally contextualized food choices.
- `evidence_level`: Scientific rigor classification.

## Usage Example
You can use the included `generar_reporte.py` script to simulate how the database can be used to generate personalized nutrigenetic reports:

```bash
python generar_reporte.py
```

This will process a simulated patient profile and output dietary recommendations based on the **Mexican Genome model**.

## References
Citations include key studies spanning from classic genetics (Grant et al., 2006) to recent nutrigenomics research in Mexico (Panduro et al., 2011; Leal-Mercado et al., 2025).
