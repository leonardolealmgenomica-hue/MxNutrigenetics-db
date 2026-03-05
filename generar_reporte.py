# -*- coding: utf-8 -*-
"""
generar_reporte.py
==================
Script de ejemplo para demostrar el uso de la base de datos de SNPs Mexican Genome.
Simula el análisis de un paciente y genera un reporte personalizado.
"""

import sys
import random
from datetime import datetime

# Configurar salida de consola para evitar errores de codificación en Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from snp_db import SNP_DATABASE

def simular_paciente(nombre):
    """
    Simula genotipos aleatorios para un paciente basados en la base de datos.
    """
    perfil = []
    for snp in SNP_DATABASE:
        # Simplificación: 25% riesgo homocigoto, 50% heterocigoto, 25% protector
        opciones = snp["risk_genotypes"] + snp["protective_genotypes"]
        genotipo = random.choice(opciones)
        
        es_riesgo = genotipo in snp["risk_genotypes"]
        
        perfil.append({
            "rs_id": snp["rs_id"],
            "gene": snp["gene"],
            "area": snp["area"],
            "genotype": genotipo,
            "is_risk": es_riesgo,
            "snp_data": snp
        })
    return perfil

def generar_reporte_consola(nombre, perfil):
    print("=" * 80)
    print(f"REPORTE NUTRIGENÉTICO PERSONALIZADO - MODELO MEXICAN GENOME")
    print(f"Paciente: {nombre}")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print("\nRESUMEN DE VARIANTE DE RIESGO DETECTADAS:\n")

    alertas = [p for p in perfil if p["is_risk"]]
    
    if not alertas:
        print("[OK] No se detectaron variantes de alto riesgo en las áreas analizadas.")
    else:
        for al in alertas:
            data = al["snp_data"]
            print(f"[!] ÁREA: {al['area'].upper()}")
            print(f"    Variante: {al['gene']} ({al['rs_id']}) | Genotipo: {al['genotype']}")
            print(f"    Efecto: {data['effect'][:120]}...")
            
            print("\n    RECOMENDACIONES NUTRICIONALES (DIETA MEXICANA):")
            rec_alimentos = ", ".join(data["foods_recommended"][:3])
            print(f"    - Priorizar: {rec_alimentos}")
            
            evitar = ", ".join(data["foods_avoid"][:2])
            print(f"    - Evitar: {evitar}")
            
            nutrientes = ", ".join([n["nutrient"] for n in data["nutrients_up"][:2]])
            print(f"    - Nutrientes clave: {nutrientes}")
            print("-" * 40)

    print("\n" + "=" * 80)
    print("AVISO: Este es un reporte simulado con fines educativos y de demostración.")
    print("=" * 80)

if __name__ == "__main__":
    nombre_paciente = "Juan Perez (Simulacion)"
    print(f"Procesando datos geneticos para {nombre_paciente}...")
    perfil_paciente = simular_paciente(nombre_paciente)
    generar_reporte_consola(nombre_paciente, perfil_paciente)
