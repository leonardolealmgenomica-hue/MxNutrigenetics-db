"""
modules/snp_db.py
=================
Base de datos curada de SNPs relevantes para nutrigenética
en población mexicana (modelo Mexican Genome).

Cada entrada contiene:
  - rs_id          : Identificador del SNP en dbSNP
  - gene           : Gen donde se ubica
  - area           : Área metabólica
  - risk_allele    : Alelo de riesgo
  - risk_genotypes : Genotipos de riesgo (lista)
  - maf_mexican    : Minor allele frequency en población mexicana (MXL 1000 Genomes)
  - effect         : Efecto funcional del genotipo de riesgo
  - nutrients_up   : Nutrientes a aumentar (con justificación)
  - nutrients_down : Nutrientes a reducir
  - foods_recommended : Alimentos de la dieta mexicana recomendados
  - foods_avoid    : Alimentos a limitar
  - evidence_level : A (meta-análisis/ECA), B (estudios cohorte), C (in vitro/in vivo)
  - references     : Referencias clave
"""

SNP_DATABASE = [

    # ══════════════════════════════════════════════════════════════
    # ÁREA 1: METABOLISMO DE CARBOHIDRATOS / GLUCOSA
    # ══════════════════════════════════════════════════════════════
    {
        "rs_id": "rs7903146",
        "gene": "TCF7L2",
        "gene_full": "Transcription Factor 7-Like 2",
        "area": "Metabolismo de carbohidratos",
        "chromosome": "10",
        "risk_allele": "T",
        "risk_genotypes": ["TT", "CT"],
        "protective_genotypes": ["CC"],
        "maf_mexican": 0.28,
        "effect": (
            "Alelo T asociado a reducción de la secreción de insulina postprandial, "
            "mayor riesgo de diabetes tipo 2 (OR 1.37-1.45). "
            "Efecto más pronunciado en población latinoamericana/mexicana. "
            "Altera la expresión de TCF7L2 en células beta pancreáticas, "
            "reduciendo la respuesta insulínica al GLP-1."
        ),
        "nutrients_up": [
            {"nutrient": "Fibra soluble", "dose": "≥25 g/día",
             "reason": "Reduce índice glucémico, mejora sensibilidad a insulina vía GLP-1"},
            {"nutrient": "Magnesio", "dose": "350-400 mg/día",
             "reason": "Cofactor de glucoquinasa, mejora señalización insulínica"},
            {"nutrient": "Polifenoles (antocianinas)", "dose": "≥200 mg/día",
             "reason": "Inhiben α-glucosidasa, reducen glucemia postprandial"},
        ],
        "nutrients_down": [
            {"nutrient": "Carbohidratos refinados", "reason": "Exacerban deficiencia secretora de insulina"},
            {"nutrient": "Fructosa libre (refrescos)", "reason": "Bypass insulínico, lipogénesis hepática"},
        ],
        "foods_recommended": [
            "Frijoles negros / pintos (fibra soluble, magnesio)",
            "Maíz azul / morado (antocianinas)",
            "Nopal (mucílagos, fibra soluble)",
            "Chía (fibra, ALA)",
            "Quelites / verdolagas (magnesio, fibra)",
            "Agua de jamaica (antocianinas)",
        ],
        "foods_avoid": [
            "Pan blanco, tortillas de harina refinada",
            "Refrescos azucarados",
            "Jugos industrializados",
        ],
        "evidence_level": "A",
        "references": [
            "Grant SF et al. Nat Genet 2006",
            "Duval C et al. Diabetes 2011",
            "Tapia-Conyer R et al. Salud Publica Mex 2016",
        ],
    },

    {
        "rs_id": "rs1801282",
        "gene": "PPARG",
        "gene_full": "Peroxisome Proliferator-Activated Receptor Gamma",
        "area": "Metabolismo de carbohidratos",
        "chromosome": "3",
        "risk_allele": "G",
        "risk_genotypes": ["GG"],
        "protective_genotypes": ["CG", "CC"],
        "maf_mexican": 0.12,
        "effect": (
            "Variante Pro12Ala (C→G). El alelo G (Ala) es protector en europeos "
            "pero su interacción con dieta alta en grasa saturada en mexicanos "
            "aumenta riesgo de resistencia a insulina y MASLD. "
            "PPARγ regula diferenciación adipocítica y sensibilidad insulínica."
        ),
        "nutrients_up": [
            {"nutrient": "Ácidos grasos monoinsaturados (MUFA)", "dose": "15-20% kcal",
             "reason": "Activadores naturales de PPARγ, mejoran sensibilidad insulínica"},
            {"nutrient": "Omega-3 (ALA/EPA/DHA)", "dose": "1-2 g/día",
             "reason": "Ligandos de PPARγ, reducen inflamación adiposa"},
            {"nutrient": "Polifenoles de tomate (licopeno)", "dose": "10-15 mg/día",
             "reason": "Modulan expresión PPARγ, reducen adipogénesis"},
        ],
        "nutrients_down": [
            {"nutrient": "Grasa saturada", "reason": "Activa PPARγ proinflamatorio, resistencia insulínica"},
            {"nutrient": "Grasas trans", "reason": "Antagonistas PPARγ, dislipidemia"},
        ],
        "foods_recommended": [
            "Aguacate (MUFA, fitosteroles)",
            "Semillas de chía / linaza (ALA omega-3)",
            "Sardinas / atún (EPA/DHA)",
            "Tomate (licopeno)",
            "Aceite de aguacate (MUFA)",
            "Nuez de castilla / pecan (MUFA, omega-3)",
        ],
        "foods_avoid": [
            "Manteca de cerdo, chicharrón",
            "Margarina, comida procesada con grasas trans",
        ],
        "evidence_level": "A",
        "references": [
            "Deeb SS et al. Nat Genet 1998",
            "Lindi V et al. Diabetologia 2002",
            "Roman S et al. Ann Hepatol 2010",
        ],
    },

    {
        "rs_id": "rs5219",
        "gene": "KCNJ11",
        "gene_full": "Potassium Inwardly Rectifying Channel Subfamily J Member 11",
        "area": "Metabolismo de carbohidratos",
        "chromosome": "11",
        "risk_allele": "T",
        "risk_genotypes": ["TT", "CT"],
        "protective_genotypes": ["CC"],
        "maf_mexican": 0.38,
        "effect": (
            "Variante E23K en canal de potasio Kir6.2 de células β pancreáticas. "
            "Alelo K (T) reduce respuesta insulínica al ATP, alterando secreción "
            "de insulina glucosa-dependiente. Alta frecuencia en mexicanos."
        ),
        "nutrients_up": [
            {"nutrient": "Cromo", "dose": "200-400 µg/día",
             "reason": "Potencia señal insulínica post-receptor"},
            {"nutrient": "Zinc", "dose": "10-15 mg/día",
             "reason": "Cofactor síntesis/secreción insulina en célula β"},
            {"nutrient": "Fibra insoluble", "dose": "≥15 g/día",
             "reason": "Reduce carga glucémica, protege célula β"},
        ],
        "nutrients_down": [
            {"nutrient": "Alcohol", "reason": "Inhibe secreción insulínica en portadores K"},
            {"nutrient": "Carbohidratos de alto índice glucémico", "reason": "Sobrecarga celula β"},
        ],
        "foods_recommended": [
            "Semillas de ajonjolí / pepitas de calabaza (zinc, cromo)",
            "Frijoles (fibra insoluble, cromo)",
            "Nopal asado (fibra, reduce IG)",
            "Amaranto (zinc, proteína completa)",
            "Tuna / xoconostle (fibra, bajo IG)",
        ],
        "foods_avoid": [
            "Bebidas alcohólicas",
            "Arroz blanco, pan blanco, tortilla de harina",
        ],
        "evidence_level": "A",
        "references": [
            "Gloyn AL et al. Diabetes 2003",
            "Florez JC et al. N Engl J Med 2004",
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ÁREA 2: METABOLISMO LIPÍDICO
    # ══════════════════════════════════════════════════════════════
    {
        "rs_id": "rs429358",
        "gene": "APOE",
        "gene_full": "Apolipoprotein E",
        "area": "Metabolismo lipídico",
        "chromosome": "19",
        "risk_allele": "C",
        "risk_genotypes": ["CC (ε4/ε4)", "TC (ε3/ε4)"],
        "protective_genotypes": ["TT (ε3/ε3 o ε2/ε3)"],
        "maf_mexican": 0.11,
        "effect": (
            "Alelo ε4 (C en rs429358) reduce clearance de LDL-colesterol, "
            "aumenta colesterol total 10-15 mg/dL por alelo. "
            "En mexicanos con dieta alta en grasa saturada el efecto es mayor. "
            "También asociado a mayor riesgo de Alzheimer y MASLD."
        ),
        "nutrients_up": [
            {"nutrient": "Fitosteroles", "dose": "2 g/día",
             "reason": "Compiten con colesterol en absorción intestinal, reducen LDL 10-15%"},
            {"nutrient": "Fibra soluble (beta-glucanos)", "dose": "≥10 g/día",
             "reason": "Secuestra ácidos biliares, reduce reabsorción de colesterol"},
            {"nutrient": "Omega-3 (EPA+DHA)", "dose": "2-4 g/día",
             "reason": "Reduce triglicéridos 20-30%, modula expresión APOE"},
            {"nutrient": "Polifenoles (resveratrol)", "dose": "≥50 mg/día",
             "reason": "Reduce oxidación LDL, expresión PCSK9"},
        ],
        "nutrients_down": [
            {"nutrient": "Grasa saturada", "reason": "Efecto hiperlipemiante 3x mayor en portadores ε4"},
            {"nutrient": "Colesterol dietético >300 mg/día", "reason": "Mayor absorción en ε4"},
            {"nutrient": "Alcohol", "reason": "Aumenta VLDL, interacción negativa con APOE4"},
        ],
        "foods_recommended": [
            "Aguacate (fitosteroles, MUFA)",
            "Frijoles (beta-glucanos, fibra soluble)",
            "Sardinas / macarela (EPA/DHA)",
            "Cacahuate mexicano (resveratrol)",
            "Maíz (fibra, fitosteroles)",
            "Semillas de girasol (vitamina E, fitosteroles)",
        ],
        "foods_avoid": [
            "Carnes procesadas (tocino, embutidos)",
            "Quesos grasos, crema entera",
            "Vísceras (hígado, sesos) en exceso",
        ],
        "evidence_level": "A",
        "references": [
            "Minihane AM et al. Am J Clin Nutr 2007",
            "Corella D et al. J Lipid Res 2001",
            "Roman S et al. World J Gastroenterol 2013",
        ],
    },

    {
        "rs_id": "rs174537",
        "gene": "FADS1",
        "gene_full": "Fatty Acid Desaturase 1",
        "area": "Metabolismo lipídico",
        "chromosome": "11",
        "risk_allele": "T",
        "risk_genotypes": ["TT"],
        "protective_genotypes": ["GG", "GT"],
        "maf_mexican": 0.27,
        "effect": (
            "Alelo T reduce actividad de delta-5 desaturasa (FADS1), "
            "limitando conversión de ALA → EPA → DHA. "
            "Portadores TT tienen 30-40% menos DHA plasmático con misma ingesta. "
            "Aumenta ratio AA/EPA, estado proinflamatorio basal."
        ),
        "nutrients_up": [
            {"nutrient": "EPA+DHA preformado", "dose": "≥1 g/día de EPA+DHA",
             "reason": "No dependen de la conversión FADS1, suplementación directa necesaria"},
            {"nutrient": "ALA (ácido alfa-linolénico)", "dose": "≥3 g/día",
             "reason": "Mayor ingesta compensa baja conversión"},
            {"nutrient": "Vitamina B6", "dose": "2-3 mg/día",
             "reason": "Cofactor de la vía de desaturación"},
        ],
        "nutrients_down": [
            {"nutrient": "Omega-6 en exceso (aceite de maíz/girasol >10%kcal)",
             "reason": "Compiten con omega-3 por FADS1, empeoran ratio AA/EPA"},
        ],
        "foods_recommended": [
            "Sardinas, atún, macarela (EPA/DHA directo)",
            "Chía / linaza molida (ALA)",
            "Algas marinas / espirulina (DHA de fuente vegetal)",
            "Quelites / verdolagas (ALA, omega-3 vegetal)",
            "Nuez de castilla (ALA)",
        ],
        "foods_avoid": [
            "Aceite de maíz en grandes cantidades",
            "Frituras industriales (omega-6 oxidado)",
        ],
        "evidence_level": "B",
        "references": [
            "Tanaka T et al. PLoS Genet 2009",
            "Mathias RA et al. Am J Hum Genet 2011",
        ],
    },

    {
        "rs_id": "rs662799",
        "gene": "APOA5",
        "gene_full": "Apolipoprotein A-V",
        "area": "Metabolismo lipídico",
        "chromosome": "11",
        "risk_allele": "G",
        "risk_genotypes": ["GG", "AG"],
        "protective_genotypes": ["AA"],
        "maf_mexican": 0.22,
        "effect": (
            "Alelo G reduce expresión de APOA5, aumentando triglicéridos séricos "
            "20-50%. Muy prevalente en mexicanos. Asociado a hipertrigliceridemia "
            "familiar, pancreatitis y MASLD. Interacción fuerte con consumo "
            "de carbohidratos refinados y alcohol."
        ),
        "nutrients_up": [
            {"nutrient": "Omega-3 (EPA+DHA)", "dose": "3-4 g/día",
             "reason": "Reduce triglicéridos 25-30% activando PPARα → lipolisis VLDL"},
            {"nutrient": "Fibra soluble", "dose": "≥15 g/día",
             "reason": "Reduce absorción de grasas y síntesis hepática de VLDL"},
            {"nutrient": "Niacina (B3)", "dose": "Alimentaria (no suplemento sin supervisión)",
             "reason": "Reduce síntesis hepática de VLDL-TG"},
        ],
        "nutrients_down": [
            {"nutrient": "Fructosa/sacarosa", "reason": "Principal inductor de síntesis hepática de TG"},
            {"nutrient": "Alcohol", "reason": "Inhibe oxidación de ácidos grasos, eleva TG severamente"},
            {"nutrient": "Carbohidratos refinados", "reason": "Lipogénesis de novo hepática"},
        ],
        "foods_recommended": [
            "Sardinas / atún (omega-3)",
            "Chía / linaza (ALA, fibra)",
            "Frijoles / lentejas (fibra soluble)",
            "Aguacate (MUFA, sin efecto en TG)",
            "Verduras no almidonadas (nopales, calabaza)",
            "Cacahuate (niacina, MUFA)",
        ],
        "foods_avoid": [
            "Refrescos, jugos de fruta azucarados",
            "Bebidas alcohólicas",
            "Postres con azúcar, pan dulce",
            "Frutas en almíbar",
        ],
        "evidence_level": "A",
        "references": [
            "Pennacchio LA et al. Science 2001",
            "Moreno-Luna R et al. Clin Nutr 2007",
            "Aguilar-Salinas CA et al. J Lipid Res 2005",
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ÁREA 3: RESPUESTA INFLAMATORIA
    # ══════════════════════════════════════════════════════════════
    {
        "rs_id": "rs1800629",
        "gene": "TNF",
        "gene_full": "Tumor Necrosis Factor Alpha",
        "area": "Respuesta inflamatoria",
        "chromosome": "6",
        "risk_allele": "A",
        "risk_genotypes": ["AA", "GA"],
        "protective_genotypes": ["GG"],
        "maf_mexican": 0.18,
        "effect": (
            "Polimorfismo -308G>A en promotor de TNF-α. Alelo A aumenta "
            "transcripción de TNF-α 2-7 veces. Asociado a mayor inflamación "
            "sistémica, resistencia insulínica, MASLD y progresión de hepatitis "
            "viral. Muy relevante en contexto GENOMEX."
        ),
        "nutrients_up": [
            {"nutrient": "Curcumina", "dose": "500-1000 mg/día (con pimienta negra)",
             "reason": "Inhibe NFκB → reduce transcripción TNF-α directamente"},
            {"nutrient": "Omega-3 (EPA)", "dose": "2-3 g/día",
             "reason": "Compite con AA por COX-2, reduce producción de TNF-α"},
            {"nutrient": "Vitamina D", "dose": "1000-2000 UI/día",
             "reason": "VDR modula expresión TNF-α y NFκB"},
            {"nutrient": "Polifenoles (quercetina, luteolina)", "dose": "≥100 mg/día",
             "reason": "Inhiben NFκB e IKK, reducen expresión de citocinas proinflamatorias"},
        ],
        "nutrients_down": [
            {"nutrient": "Grasa saturada (>10% kcal)", "reason": "Activa TLR4 → NFκB → TNF-α"},
            {"nutrient": "Azúcar refinada en exceso", "reason": "AGEs activan NFκB"},
        ],
        "foods_recommended": [
            "Cúrcuma / turmeric con pimienta negra",
            "Chile mexicano (capsaicina inhibe NFκB)",
            "Sardinas / atún (EPA omega-3)",
            "Orégano mexicano (luteolina-7-O-glucósido)",
            "Tomate (licopeno antiinflamatorio)",
            "Cacao oscuro ≥70% (epicatequinas, polifenoles)",
            "Guayaba (vitamina C, quercetina)",
        ],
        "foods_avoid": [
            "Carnes procesadas (activadores TLR4)",
            "Aceites vegetales refinados en exceso",
            "Azúcar y harinas refinadas",
        ],
        "evidence_level": "A",
        "references": [
            "Panduro A et al. Ann Hepatol 2011",
            "Roman S et al. J Hepatol 2010",
            "Leal-Mercado L et al. IJMS 2025",
        ],
    },

    {
        "rs_id": "rs1800795",
        "gene": "IL6",
        "gene_full": "Interleukin 6",
        "area": "Respuesta inflamatoria",
        "chromosome": "7",
        "risk_allele": "C",
        "risk_genotypes": ["CC"],
        "protective_genotypes": ["GG", "GC"],
        "maf_mexican": 0.41,
        "effect": (
            "Polimorfismo -174G>C en promotor de IL-6. Alelo C reduce expresión "
            "de IL-6 en condiciones basales pero aumenta en contexto inflamatorio. "
            "En mexicanos asociado a mayor susceptibilidad a MASLD y respuesta "
            "inflamatoria exacerbada ante dieta hipercalórica."
        ),
        "nutrients_up": [
            {"nutrient": "Magnesio", "dose": "350-400 mg/día",
             "reason": "Reduce IL-6 circulante, cofactor antiinflamatorio"},
            {"nutrient": "Vitamina E (tocoferoles)", "dose": "200-400 UI/día",
             "reason": "Reduce expresión IL-6 en adipocitos y hepatocitos"},
            {"nutrient": "Resveratrol", "dose": "100-250 mg/día",
             "reason": "Inhibe STAT3 → reduce señalización IL-6 proinflamatoria"},
        ],
        "nutrients_down": [
            {"nutrient": "Sodio en exceso (>2.3 g/día)", "reason": "Activa NLRP3 → IL-6 e IL-1β"},
            {"nutrient": "Grasa trans", "reason": "Activa NFκB, aumenta IL-6 sistémica"},
        ],
        "foods_recommended": [
            "Aguacate (vitamina E, MUFA antiinflamatorio)",
            "Semillas de girasol (vitamina E)",
            "Cacahuate mexicano (resveratrol)",
            "Frijoles (magnesio)",
            "Amaranto (magnesio, antiinflamatorio)",
            "Cacao (polifenoles, magnesio)",
        ],
        "foods_avoid": [
            "Alimentos ultra-procesados (sodio oculto)",
            "Margarina, galletas industriales (grasas trans)",
        ],
        "evidence_level": "B",
        "references": [
            "Fishman D et al. J Clin Invest 1998",
            "Roman S et al. Ann Hepatol 2013",
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ÁREA 4: METABOLISMO DE MICRONUTRIENTES
    # ══════════════════════════════════════════════════════════════
    {
        "rs_id": "rs1801133",
        "gene": "MTHFR",
        "gene_full": "Methylenetetrahydrofolate Reductase",
        "area": "Metabolismo de micronutrientes",
        "chromosome": "1",
        "risk_allele": "T",
        "risk_genotypes": ["TT"],
        "protective_genotypes": ["CC", "CT"],
        "maf_mexican": 0.47,
        "effect": (
            "Variante C677T. Alelo T reduce actividad MTHFR 35-70%, "
            "elevando homocisteína plasmática. Muy prevalente en mexicanos "
            "(hasta 47% MAF). Reduce producción de 5-MTHF (folato activo), "
            "afectando metilación del ADN, síntesis de SAM y metabolismo "
            "de neurotransmisores. Riesgo cardiovascular, defectos del tubo neural."
        ),
        "nutrients_up": [
            {"nutrient": "Folato (5-MTHF forma activa)", "dose": "600-1000 µg/día",
             "reason": "Forma activa no requiere conversión por MTHFR deficiente"},
            {"nutrient": "Vitamina B12 (cobalamina)", "dose": "≥2.4 µg/día alimentaria / 500 µg supl.",
             "reason": "Cofactor de metionina sintasa, esencial para remetilación de homocisteína"},
            {"nutrient": "Vitamina B6 (piridoxina)", "dose": "2-3 mg/día",
             "reason": "Ruta alternativa de transulfuración de homocisteína"},
            {"nutrient": "Riboflavina (B2)", "dose": "2-4 mg/día",
             "reason": "Cofactor de MTHFR, estabiliza la enzima residual"},
            {"nutrient": "Colina", "dose": "≥425-550 mg/día",
             "reason": "Ruta alternativa de metilación (PEMT), protege hígado"},
        ],
        "nutrients_down": [
            {"nutrient": "Alcohol", "reason": "Antagonista del folato, eleva homocisteína"},
            {"nutrient": "Café en exceso (>4 tazas/día)", "reason": "Aumenta homocisteína en portadores TT"},
        ],
        "foods_recommended": [
            "Frijoles negros / bayos (folato natural, colina)",
            "Quelites / espinacas mexicanas (folato)",
            "Hígado de res (B12, folato, colina) — con moderación",
            "Huevo (colina, B12)",
            "Sardinas (B12, omega-3)",
            "Amaranto (B2, B6, folato)",
            "Semillas de girasol (B6)",
        ],
        "foods_avoid": [
            "Bebidas alcohólicas",
            "Café en exceso",
        ],
        "evidence_level": "A",
        "references": [
            "Frosst P et al. Nat Genet 1995",
            "Wilcken B et al. J Med Genet 2003",
            "Velázquez-Arellano A et al. Rev Invest Clin 2012",
        ],
    },

    {
        "rs_id": "rs2228570",
        "gene": "VDR",
        "gene_full": "Vitamin D Receptor",
        "area": "Metabolismo de micronutrientes",
        "chromosome": "12",
        "risk_allele": "C",
        "risk_genotypes": ["CC"],
        "protective_genotypes": ["TT", "TC"],
        "maf_mexican": 0.33,
        "effect": (
            "Polimorfismo FokI en VDR. Alelo C (f) produce proteína VDR más corta "
            "y menos eficiente. Reduce respuesta celular a vitamina D. "
            "En mexicanos asociado a mayor riesgo de raquitismo, osteoporosis, "
            "infecciones respiratorias, MASLD y cáncer de colon."
        ),
        "nutrients_up": [
            {"nutrient": "Vitamina D3 (colecalciferol)", "dose": "2000-4000 UI/día",
             "reason": "Mayor ingesta compensa menor eficiencia del receptor VDR-f"},
            {"nutrient": "Calcio", "dose": "1000-1200 mg/día",
             "reason": "Absorción dependiente de VDR, requiere compensación"},
            {"nutrient": "Magnesio", "dose": "350-400 mg/día",
             "reason": "Cofactor de la hidroxilación de vitamina D a forma activa"},
            {"nutrient": "Vitamina K2 (MK-7)", "dose": "100-200 µg/día",
             "reason": "Dirige calcio a hueso, trabaja sinérgicamente con VDR"},
        ],
        "nutrients_down": [
            {"nutrient": "Fitatos en exceso (sin remojar)", "reason": "Reducen absorción de calcio"},
        ],
        "foods_recommended": [
            "Sardinas / atún enlatado (vitamina D, calcio)",
            "Huevo (vitamina D, K2)",
            "Hongos expuestos al sol / huitlacoche (vitamina D vegetal)",
            "Frijoles remojados y cocidos (calcio biodisponible)",
            "Semillas de ajonjolí (calcio)",
            "Verdolagas / quelites (calcio, magnesio)",
            "Leche de vaca / queso cotija (calcio)",
        ],
        "foods_avoid": [
            "Frijoles sin remojar en exceso (fitatos)",
            "Bebidas con fosfatos (refrescos de cola) — reducen absorción calcio",
        ],
        "evidence_level": "B",
        "references": [
            "Uitterlinden AG et al. Gene 2004",
            "Ramos-Lopez E et al. Exp Clin Endocrinol 2007",
        ],
    },

    {
        "rs_id": "rs1799945",
        "gene": "HFE",
        "gene_full": "Homeostatic Iron Regulator",
        "area": "Metabolismo de micronutrientes",
        "chromosome": "6",
        "risk_allele": "G",
        "risk_genotypes": ["GG"],
        "protective_genotypes": ["AA", "AG"],
        "maf_mexican": 0.06,
        "effect": (
            "Variante H63D en HFE. Alelo G aumenta absorción intestinal de hierro, "
            "riesgo de sobrecarga de hierro (hemocromatosis leve-moderada). "
            "El exceso de hierro genera estrés oxidativo hepático, "
            "acelerando fibrosis en MASLD y hepatitis viral."
        ),
        "nutrients_up": [
            {"nutrient": "Polifenoles (taninos)", "dose": "Con cada comida",
             "reason": "Quelantes naturales del hierro, reducen absorción"},
            {"nutrient": "Calcio", "dose": "Con comidas ricas en hierro",
             "reason": "Compite con hierro en transporte intestinal"},
            {"nutrient": "Vitamina E", "dose": "200-400 UI/día",
             "reason": "Antioxidante, neutraliza estrés oxidativo por sobrecarga de hierro"},
        ],
        "nutrients_down": [
            {"nutrient": "Vitamina C con carnes rojas", "reason": "Aumenta absorción de hierro hem"},
            {"nutrient": "Suplementos de hierro", "reason": "Contraindicados sin déficit documentado"},
            {"nutrient": "Alcohol", "reason": "Potencia daño oxidativo hepático por hierro"},
        ],
        "foods_recommended": [
            "Té de hierbas mexicanas (taninos quelantes) con comidas",
            "Café negro (ácido clorogénico reduce absorción hierro)",
            "Frijoles (hierro no-hem, menor absorción)",
            "Aguacate (vitamina E)",
            "Semillas de girasol (vitamina E)",
        ],
        "foods_avoid": [
            "Hígado / vísceras (hierro hem concentrado)",
            "Suplementos de hierro",
            "Carnes rojas en exceso",
        ],
        "evidence_level": "B",
        "references": [
            "Feder JN et al. Nat Genet 1996",
            "Roman S et al. Liver Int 2009",
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ÁREA 5: RIESGO DE MASLD / ENFERMEDAD HEPÁTICA
    # ══════════════════════════════════════════════════════════════
    {
        "rs_id": "rs738409",
        "gene": "PNPLA3",
        "gene_full": "Patatin-Like Phospholipase Domain Containing 3",
        "area": "Riesgo de MASLD",
        "chromosome": "22",
        "risk_allele": "G",
        "risk_genotypes": ["GG"],
        "protective_genotypes": ["CC", "CG"],
        "maf_mexican": 0.49,
        "effect": (
            "Variante I148M. El alelo G (Met) es el principal factor genético "
            "de MASLD en mexicanos (MAF ~49%, el más alto globalmente). "
            "Reduce actividad lipolítica de PNPLA3 en gotas lipídicas hepáticas, "
            "acumulando triglicéridos. Riesgo 3.26x de MASLD en homocigotos GG. "
            "Asociado a esteatosis, MASH, fibrosis y HCC en mexicanos."
        ),
        "nutrients_up": [
            {"nutrient": "Omega-3 (EPA+DHA)", "dose": "2-4 g/día",
             "reason": "Activa PPARα → aumenta oxidación de AG hepáticos, reduce esteatosis"},
            {"nutrient": "Vitamina E (alfa-tocoferol)", "dose": "800 UI/día supervisado",
             "reason": "Reduce estrés oxidativo hepático, mejora histología en MASH"},
            {"nutrient": "Colina", "dose": "≥500 mg/día",
             "reason": "Esencial para exportación de VLDL hepático, previene esteatosis"},
            {"nutrient": "Cafeína (café negro sin azúcar)", "dose": "2-3 tazas/día",
             "reason": "Asociada inversamente con fibrosis hepática en portadores PNPLA3-G"},
            {"nutrient": "Fructooligosacáridos (prebióticos)", "dose": "≥5 g/día",
             "reason": "Modulan microbiota, reducen producción de LPS → inflamación hepática"},
        ],
        "nutrients_down": [
            {"nutrient": "Fructosa libre", "reason": "Lipogénesis de novo potenciada en PNPLA3-GG"},
            {"nutrient": "Grasa saturada", "reason": "Acumula triglicéridos en gotas lipídicas"},
            {"nutrient": "Alcohol", "reason": "Sinergia destructiva con PNPLA3-G, acelera fibrosis"},
            {"nutrient": "Carbohidratos refinados", "reason": "Sustrato para lipogénesis hepática"},
        ],
        "foods_recommended": [
            "Sardinas / atún / macarela (EPA+DHA)",
            "Aguacate (MUFA, vitamina E, colina)",
            "Huevo (colina — si no hay hipercolesterolemia)",
            "Café negro sin azúcar (cafeína hepatoprotectora)",
            "Frijoles / chía / nopal (FOS, fibra prebiótica)",
            "Semillas de girasol / aguacate (vitamina E)",
            "Tomate (licopeno, antioxidante hepático)",
        ],
        "foods_avoid": [
            "Refrescos y jugos azucarados",
            "Pan dulce, pasteles, harinas refinadas",
            "Bebidas alcohólicas — contraindicadas",
            "Manteca, chicharrón, carnitas en exceso",
        ],
        "evidence_level": "A",
        "references": [
            "Romeo S et al. Nat Genet 2008",
            "Aguilar-Olivos NE et al. Ann Hepatol 2015",
            "Leal-Mercado L et al. IJMS 2025",
            "Roman S et al. Hepatology 2010",
        ],
    },

    {
        "rs_id": "rs2294918",
        "gene": "PNPLA3",
        "gene_full": "Patatin-Like Phospholipase Domain Containing 3",
        "area": "Riesgo de MASLD",
        "chromosome": "22",
        "risk_allele": "A",
        "risk_genotypes": ["AA"],
        "protective_genotypes": ["GG", "GA"],
        "maf_mexican": 0.38,
        "effect": (
            "Segunda variante PNPLA3 (E434K). Modifica la proteína PNPLA3 "
            "de forma independiente a rs738409. En combinación con rs738409-G "
            "aumenta riesgo de fibrosis avanzada. Relevante en haplotipos mexicanos."
        ),
        "nutrients_up": [
            {"nutrient": "Silimarina (cardo mariano)", "dose": "140-420 mg/día",
             "reason": "Hepatoprotector, reduce NF-κB hepático y fibrosis"},
            {"nutrient": "Omega-3", "dose": "2-3 g/día", "reason": "Ver rs738409"},
            {"nutrient": "Antioxidantes totales (ORAC)", "dose": "Dieta alta en polifenoles",
             "reason": "Reduce estrés oxidativo, frena activación de HSC"},
        ],
        "nutrients_down": [
            {"nutrient": "Fructosa / alcohol", "reason": "Mismos mecanismos que rs738409"},
        ],
        "foods_recommended": [
            "Cardo mariano (silimarina)",
            "Cacao oscuro (antioxidantes hepáticos)",
            "Maíz morado / frijol negro (antocianinas antiinflamatorias)",
            "Chía / linaza (omega-3 ALA)",
        ],
        "foods_avoid": ["Alcohol", "Fructosa libre", "Ultraprocesados"],
        "evidence_level": "B",
        "references": [
            "Sookoian S et al. Hepatology 2009",
            "Roman S et al. Ann Hepatol 2015",
        ],
    },

    {
        "rs_id": "rs58542926",
        "gene": "TM6SF2",
        "gene_full": "Transmembrane 6 Superfamily Member 2",
        "area": "Riesgo de MASLD",
        "chromosome": "19",
        "risk_allele": "A",
        "risk_genotypes": ["AA", "CA"],
        "protective_genotypes": ["CC"],
        "maf_mexican": 0.07,
        "effect": (
            "Variante E167K. Reduce exportación hepática de VLDL, acumulando "
            "lípidos en hepatocitos. Paradójicamente reduce riesgo cardiovascular "
            "pero aumenta riesgo de MASLD, fibrosis y HCC. "
            "Efecto independiente de PNPLA3."
        ),
        "nutrients_up": [
            {"nutrient": "Colina + fosfatidilcolina", "dose": "≥600 mg/día",
             "reason": "Componente esencial de VLDL para exportar lípidos hepáticos"},
            {"nutrient": "Omega-3", "dose": "2-3 g/día",
             "reason": "Activa PPARα, oxidación hepática de ácidos grasos"},
            {"nutrient": "Vitamina E", "dose": "400-800 UI/día",
             "reason": "Reduce peroxidación lipídica en hepatocitos TM6SF2-A"},
        ],
        "nutrients_down": [
            {"nutrient": "Alcohol", "reason": "Potencia acumulación lipídica"},
            {"nutrient": "Grasa saturada", "reason": "Sobrecarga exportación VLDL deficiente"},
        ],
        "foods_recommended": [
            "Huevo (fosfatidilcolina, colina)",
            "Sardinas (colina, EPA/DHA)",
            "Aguacate (MUFA, vitamina E)",
            "Soya mexicana / edamame (lecitina, colina)",
        ],
        "foods_avoid": ["Alcohol", "Carnitas, chicharrón", "Ultraprocesados grasos"],
        "evidence_level": "B",
        "references": [
            "Kozlitina J et al. Nat Genet 2014",
            "Liu YL et al. Nat Commun 2014",
        ],
    },

    # ══════════════════════════════════════════════════════════════
    # ÁREA 6: INTOLERANCIAS ALIMENTARIAS
    # ══════════════════════════════════════════════════════════════
    {
        "rs_id": "rs4988235",
        "gene": "MCM6",
        "gene_full": "Minichromosome Maintenance Complex Component 6 (regulador LCT)",
        "area": "Intolerancia a lactosa",
        "chromosome": "2",
        "risk_allele": "G",
        "risk_genotypes": ["GG"],
        "protective_genotypes": ["AA", "AG"],
        "maf_mexican": 0.82,
        "effect": (
            "Variante -13910C>T (rs4988235 A=T alelo persistencia). "
            "Alelo G (ancestral) = no persistencia de lactasa → intolerancia a lactosa. "
            "MAF ~82% en mexicanos (mayoría NO persiste lactasa). "
            "Causa distensión, diarrea y malabsorción de calcio si consumen lácteos."
        ),
        "nutrients_up": [
            {"nutrient": "Calcio no lácteo", "dose": "1000 mg/día",
             "reason": "Compensar baja absorción por evitar lácteos"},
            {"nutrient": "Vitamina D", "dose": "1000-2000 UI/día",
             "reason": "Optimizar absorción de calcio no lácteo"},
            {"nutrient": "Probióticos (Lactobacillus acidophilus)", "dose": "≥10⁹ UFC/día",
             "reason": "Producen lactasa endógena, mejoran tolerancia a pequeñas cantidades"},
        ],
        "nutrients_down": [
            {"nutrient": "Lactosa", "reason": "No tolerada — síntomas GI en GG"},
        ],
        "foods_recommended": [
            "Tortillas de maíz con cal (nixtamal — calcio biodisponible)",
            "Semillas de ajonjolí / chía (calcio)",
            "Frijoles / quelites (calcio vegetal)",
            "Sardinas con hueso (calcio)",
            "Quelites / verdolagas (calcio, magnesio)",
            "Yogurt o kéfir (lactosa reducida, si tolera)",
            "Queso añejo (bajo en lactosa, si tolera pequeñas cantidades)",
        ],
        "foods_avoid": [
            "Leche entera / descremada",
            "Helados, natillas, cremas",
            "Quesos frescos altos en lactosa",
        ],
        "evidence_level": "A",
        "references": [
            "Enattah NS et al. Nat Genet 2002",
            "Romero-Velarde E et al. Bol Med Hosp Infant Mex 2016",
        ],
    },

    {
        "rs_id": "rs762551",
        "gene": "CYP1A2",
        "gene_full": "Cytochrome P450 Family 1 Subfamily A Member 2",
        "area": "Metabolismo de cafeína",
        "chromosome": "15",
        "risk_allele": "A",
        "risk_genotypes": ["AA"],
        "protective_genotypes": ["AC", "CC"],
        "maf_mexican": 0.67,
        "effect": (
            "Alelo A = metabolizador rápido de cafeína. "
            "Alelo C = metabolizador lento → mayor exposición a cafeína. "
            "Portadores CC (lento) tienen mayor riesgo cardiovascular con café, "
            "pero portadores AA (rápido) pueden beneficiarse del café. "
            "Relevante para recomendación de café en MASLD (hepatoprotector en AA)."
        ),
        "nutrients_up": [
            {"nutrient": "Cafeína / café (para AA rápidos)", "dose": "200-400 mg/día (3-4 tazas)",
             "reason": "Metabolizadores rápidos se benefician: hepatoprotección, reduce fibrosis"},
        ],
        "nutrients_down": [
            {"nutrient": "Cafeína en exceso (para CC lentos)", "reason": "Aumenta presión arterial, riesgo CV"},
        ],
        "foods_recommended": [
            "Café negro sin azúcar (AA: hasta 4 tazas/día)",
            "Té verde / té de hierbas (CC: alternativa baja en cafeína)",
            "Cacao (teobromina, menor efecto que cafeína)",
        ],
        "foods_avoid": [
            "Café en exceso para metabolizadores lentos (CC)",
            "Bebidas energéticas (cafeína + otros estimulantes)",
        ],
        "evidence_level": "B",
        "references": [
            "Cornelis MC et al. JAMA 2006",
            "Ruhl CE et al. Hepatology 2014",
        ],
    },

    {
        "rs_id": "rs2187668",
        "gene": "HLA-DQA1",
        "gene_full": "HLA class II histocompatibility antigen, DQ alpha 1 chain",
        "area": "Intolerancia al gluten / celiaquía",
        "chromosome": "6",
        "risk_allele": "T",
        "risk_genotypes": ["TT"],
        "protective_genotypes": ["CC", "CT"],
        "maf_mexican": 0.19,
        "effect": (
            "Marcador HLA-DQ2.5 (parte del haplotipo). Necesario (no suficiente) "
            "para celiaquía. Portadores TT tienen mayor susceptibilidad a reacción "
            "inmune al gluten. En mexicanos la celiaquía está subdiagnosticada. "
            "Requiere confirmación serológica y biopsia intestinal."
        ),
        "nutrients_up": [
            {"nutrient": "Hierro", "dose": "18 mg/día (mujeres), 8 mg (hombres)",
             "reason": "Malabsorción frecuente en enteropatía por gluten"},
            {"nutrient": "Calcio + Vitamina D", "dose": "1000 mg Ca / 1500 UI D",
             "reason": "Malabsorción ósea en celiaquía activa"},
            {"nutrient": "Folato", "dose": "600-1000 µg/día",
             "reason": "Malabsorción en yeyuno afectado por gluten"},
        ],
        "nutrients_down": [
            {"nutrient": "Gluten (trigo, cebada, centeno)", "reason": "Desencadena enteropatía en celíacos"},
        ],
        "foods_recommended": [
            "Tortilla de maíz nixtamalizado (libre de gluten, alta en calcio)",
            "Tostadas de maíz, tamales de maíz",
            "Frijoles / arroz / quinoa (sin gluten)",
            "Amaranto (cereal mexicano libre de gluten, alto en hierro)",
            "Chía / linaza (sin gluten)",
            "Verduras y frutas mexicanas (todas sin gluten)",
        ],
        "foods_avoid": [
            "Pan de trigo, tortillas de harina",
            "Pasta, cebada, centeno",
            "Salsas industriales con trigo (soya con trigo, mole en polvo)",
        ],
        "evidence_level": "B",
        "references": [
            "Sollid LM et al. Nat Rev Immunol 2002",
            "Catassi C et al. Ann Med 2010",
        ],
    },
]


# ── Índice por rs_id ──────────────────────────────────────────────────────────
SNP_INDEX = {snp["rs_id"].lower(): snp for snp in SNP_DATABASE}


def get_snp(rs_id: str) -> dict | None:
    """Retorna datos de un SNP por su rs ID (case-insensitive)."""
    return SNP_INDEX.get(rs_id.lower().strip())


def list_areas() -> list[str]:
    """Lista todas las áreas metabólicas cubiertas."""
    return sorted(set(s["area"] for s in SNP_DATABASE))


def list_snps_by_area(area: str) -> list[dict]:
    """Retorna todos los SNPs de un área metabólica."""
    return [s for s in SNP_DATABASE if s["area"].lower() == area.lower()]


def list_all_rs_ids() -> list[str]:
    """Lista todos los rs IDs en la base de datos."""
    return [s["rs_id"] for s in SNP_DATABASE]


# ── Test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Total SNPs en base de datos: {len(SNP_DATABASE)}")
    print(f"\nÁreas cubiertas:")
    for area in list_areas():
        snps = list_snps_by_area(area)
        print(f"  {area}: {len(snps)} SNPs")
    print(f"\nTodos los rs IDs: {', '.join(list_all_rs_ids())}")
