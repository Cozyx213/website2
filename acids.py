import sqlite3
def insert_compound(compound_name, chemical_formula, description):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO acids(element_name, element_symbol, other_info)
        VALUES (?, ?, ? )
    ''', (compound_name, chemical_formula, description))

    conn.commit()
    conn.close()
    
common_acids = [
    ("Hydrochloric Acid", "HCl", "Strong acid used in various industrial processes."),
    ("Sulfuric Acid", "H2SO4", "Highly corrosive and widely used in the chemical industry."),
    ("Nitric Acid", "HNO3", "Used for various purposes, including in the production of fertilizers and explosives."),
    ("Acetic Acid", "CH3COOH", "Found in vinegar and used in the food industry."),
    ("Phosphoric Acid", "H3PO4", "Used in fertilizers and food additives."),
    ("Sulfurous Acid", "H2SO3", "A weak acid formed when sulfur dioxide dissolves in water."),
    ("Carbonic Acid", "H2CO3", "Forms when carbon dioxide dissolves in water, found in carbonated beverages."),
    ("Citric Acid", "C6H8O7", "Found in citrus fruits and used as a food additive and flavoring agent."),
    ("Hydrofluoric Acid", "HF", "Highly corrosive and used in etching glass and for certain chemical reactions."),
    ("Phenol", "C6H5OH", "Used as an antiseptic and in the production of plastics and pharmaceuticals."),
    ("Sulfuric Acid", "H2S2O7", "Known as oleum or fuming sulfuric acid, used in chemical synthesis."),
    ("Hydrobromic Acid", "HBr", "Strong acid used in organic synthesis and as a reagent."),
    ("Perchloric Acid", "HClO4", "Highly reactive and used in analytical chemistry."),
    ("Tartaric Acid", "C4H6O6", "Found in grapes and used in baking and winemaking."),
    ("Sulfamic Acid", "H3NSO3", "Used as a cleaning agent and descaling agent."),
    ("Oxalic Acid", "C2H2O4", "Found in many vegetables and used in cleaning and bleaching."),
    ("Hydrocyanic Acid", "HCN", "Highly toxic and used in various industrial processes."),
    ("Formic Acid", "HCOOH", "Found in ant venom and used as a preservative and in textile and leather industries."),
    ("Boric Acid", "H3BO3", "Used in various applications, including as an antiseptic and insecticide."),
    ("Chloric Acid", "HClO3", "Used in the synthesis of various chemicals and explosives."),
]

for acid in common_acids:
    name = acid[0]
    formula = acid[1]
    description = acid[2]
    insert_compound(name,formula,description)