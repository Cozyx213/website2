import sqlite3

def insert_compound(compound_name, chemical_formula, description, charge):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO polyions (element_name, element_symbol, other_info, charge)
        VALUES (?, ?, ?,? )
    ''', (compound_name, chemical_formula, description, charge))

    conn.commit()
    conn.close()
polyatomic_ions = [
    ("Acetate", "CH3CO2-", -1, "Commonly found in vinegar and acts as a weak base."),
    ("Dichromate", "Cr2O7^2-", -2, "Used in various chemical processes, including in dichromate tests."),
    ("Hypobromite", "BrO-", -1, "A chemical intermediate in the synthesis of organic compounds."),
    ("Perrhenate", "ReO4-", -1, "Used in analytical chemistry and as a catalyst."),
    ("Ammonium", "NH4+", 1, "A positively charged polyatomic ion containing nitrogen and hydrogen."),
    ("Dihydrogen Phosphate", "H2PO4-", -1, "Found in many biological processes and as a component of DNA."),
    ("Hypochlorite", "ClO-", -1, "Commonly used as a disinfectant and bleach."),
    ("Phosphate", "PO4^3-", -3, "An essential component of nucleic acids like DNA and RNA."),
    ("Arsenate", "AsO4^3-", -3, "A toxic ion often associated with contamination in groundwater."),
    ("Dihydrogen Phosphite", "H2PO3-", -1, "Used in agriculture as a phosphorus fertilizer."),
    ("Hypoiodite", "IO-", -1, "A reactive intermediate in organic synthesis."),
    ("Phosphite", "PO3^3-", -3, "Used in some chemical processes and as a reducing agent."),
    ("Arsenite", "AsO3^3-", -3, "A toxic ion, often associated with environmental pollution."),
    ("Dithionate", "S2O6^2-", -2, "Used in analytical chemistry and as an oxidizing agent."),
    ("Iodate", "IO3-", -1, "Used in iodized salt and analytical chemistry."),
    ("Plumbate", "PbO3^2-", -2, "A lead-containing ion with limited practical use."),
    ("Azide", "N3-", -1, "Commonly used in organic synthesis and explosives."),
    ("Dithionite", "S2O4^2-", -2, "Used as a reducing agent in chemistry."),
    ("Iodite", "IO2-", -1, "A rare ion used in some chemical reactions."),
    ("Plumbite", "PbO2^2-", -2, "A lead-containing ion with limited practical use."),
    ("Borate", "BO3^2-", -2, "Found in various minerals and glasses."),
    ("Ferricyanide", "Fe(CN)6^3-", -3, "Used in analytical chemistry for iron detection."),
    ("Isocyanate", "NCO-", -1, "Commonly used in the synthesis of organic compounds."),
    ("Rhenate", "ReO4^2-", -2, "Used in analytical chemistry and catalysis."),
    ("Bromate", "BrO3-", -1, "Used in some chemical processes and water treatment."),
    ("Ferrocyanide", "Fe(CN)6^4-", -4, "Used in the production of blue pigments and as an anti-caking agent."),
    ("Manganate", "MnO4^2-", -2, "Used in redox reactions and as an oxidizing agent."),
    ("Selenate", "SeO4^2-", -2, "Used in analytical chemistry and as a nutrient for some plants."),
    ("Bromite", "BrO2-", -1, "A rare ion used in some chemical reactions."),
    ("Fulminate", "CNO-", -1, "Highly explosive and used in detonators."),
    ("Nitrate", "NO3-", -1, "Found in fertilizers and explosives."),
    ("Selenite", "SeO3^2-", -2, "Used in analytical chemistry and as a nutrient for some plants."),
    ("Carbonate", "CO3^2-", -2, "Found in limestone and contributes to water hardness."),
    ("Hydrazide", "N2H3-", -1, "Used in the synthesis of various organic compounds."),
    ("Nitrite", "NO2-", -1, "Used as a food preservative and in some chemical reactions."),
    ("Silicate", "SiO3^2-", -2, "Found in minerals and makes up a large portion of Earth's crust."),
    ("Chlorate", "ClO3-", -1, "Used in the production of fireworks and matches."),
    ("Hydrogen Arsenate", "HAsO4^2-", -2, "Used in agriculture as a source of arsenic and phosphorus."),
    ("Oxalate", "C2O4^2-", -2, "Found in some plants and can form insoluble salts."),
    ("Stannate", "SnO3^2-", -2, "A tin-containing ion with limited practical use."),
    ("Chlorite", "ClO2-", -1, "Used in some water treatment processes."),
    ("Hydrogen Carbonate", "HCO3^-", -1, "Found in bicarbonate solutions and contributes to pH regulation."),
    ("Ozonide", "O3-", -1, "A rare and reactive ion containing ozone."),
    ("Stannite", "SnO2^2-", -2, "A tin-containing ion with limited practical use."),
    ("Chromate", "CrO4^2-", -2, "Used in pigments and as a corrosion inhibitor."),
    ("Hydrogen Phosphate", "HPO4^2-", -2, "A common phosphate ion found in biological systems."),
    ("Perbromate", "BrO4^-", -1, "A strong oxidizing agent used in chemical synthesis."),
    ("Sulfate", "SO4^2-", -2, "Commonly found in minerals and as a component of sulfuric acid."),
    ("Chromite", "CrO2^-", -2, "A chromium-containing ion with limited practical use."),
    ("Hydrogen Phosphite", "HPO3^2-", -2, "Used in some chemical processes as a reducing agent."),
    ("Perchlorate", "ClO4^-", -1, "A strong oxidizing agent used in various chemical applications."),
    ("Sulfite", "SO3^2-", -2, "Used in food preservation and as a reducing agent."),
    ("Citrate", "C6H5O7^3-", -3, "Used in the food and pharmaceutical industries."),
    ("Hydrogen Sulfate", "HSO4^-", -1, "An acidic sulfate ion often found in salts."),
    ("Periodate", "IO4^-", -1, "Used in analytical chemistry and as an oxidizing agent."),
    ("Superoxide", "O2^-", -1, "A highly reactive ion containing oxygen."),
    ("Cyanate", "OCN^-", -1, "Used in some chemical reactions and as a source of cyanide."),
    ("Hydrogen Sulfite", "HSO3^-", -1, "Used as a reducing agent in various chemical processes and as a food preservative."),
    ("Cyanide", "CN^-", -1, "A highly toxic ion that forms strong complexes with metals."),
    ("Hydroxide", "OH^-", -1, "A common base ion found in many solutions."),
    ("Peroxide", "O2^2-", -2, "A reactive ion containing oxygen often used as a bleach."),
    ("Thiosulfate", "S2O3^2-", -2, "Used in photography and as a reducing agent."),
    ("Tungstate", "WO4^2-", -2, "Found in various minerals and used in some industrial applications.")
]
for i in polyatomic_ions:
    name = i[0]
    formula = i[1]
    charge = i[2]
    description = i[3]
    insert_compound(name, formula, description, charge)

