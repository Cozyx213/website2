import sqlite3

def insert_compound(compound_name, chemical_formula, description=''):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO compounds (element_name, element_symbol, other_info)
        VALUES (?, ?, ?)
    ''', (compound_name, chemical_formula, description))

    conn.commit()
    conn.close()
    
compounds=[]
compounds_data = [
    ('Water', 'H2O', 'A clear, colorless liquid essential for life.'),
    ('Carbon Dioxide', 'CO2', 'A colorless gas produced during respiration and combustion.'),
    ('Glucose', 'C6H12O6', 'A simple sugar that serves as an energy source in biology.'),
    ('Methane', 'CH4', 'A colorless gas and the primary component of natural gas.'),
    ('Oxygen Gas', 'O2', 'A diatomic gas essential for respiration in many organisms.'),
    ('Ammonia', 'NH3', 'A pungent gas often used in cleaning products and refrigeration.'),
    ('Hydrochloric Acid', 'HCl', 'A strong acid used in various industrial processes.'),
    ('Sulfuric Acid', 'H2SO4', 'A strong and highly corrosive acid used in batteries and chemical synthesis.'),
    # Continue with more compounds as needed...
]
compounds_data += [
    ('Carbon Monoxide', 'CO', 'A colorless, odorless gas produced during incomplete combustion.'),
    ('Ethanol', 'C2H5OH', 'A colorless alcohol found in alcoholic beverages and used as a solvent.'),
    ('Acetic Acid', 'CH3COOH', 'A weak acid responsible for the sour taste in vinegar.'),
    ('Aspirin', 'C9H8O4', 'A common pain reliever and anti-inflammatory medication.'),
    ('Caffeine', 'C8H10N4O2', 'A stimulant found in coffee, tea, and some soft drinks.'),
    ('Calcium Carbonate', 'CaCO3', 'A white solid used as a dietary supplement and antacid.'),
    ('Sodium Bicarbonate', 'NaHCO3', 'A white crystalline powder commonly known as baking soda.'),
    ('Chlorine Gas', 'Cl2', 'A pale green gas used for water disinfection and in chemical synthesis.'),
    ('Hydrogen Peroxide', 'H2O2', 'A colorless liquid used as a disinfectant and bleaching agent.'),
    ('Methanol', 'CH3OH', 'A colorless alcohol used as a solvent and antifreeze.'),
    # Continue with more compounds as needed...
]
compounds_data += [
    ('Sodium Chloride', 'NaCl', 'Commonly known as table salt and used for seasoning and preserving food.'),
    ('Potassium Chloride', 'KCl', 'Used as a salt substitute and in medical applications.'),
    ('Calcium Oxide', 'CaO', 'A white crystalline solid known as quicklime, used in construction and manufacturing.'),
    ('Sulfur Dioxide', 'SO2', 'A colorless gas with a pungent odor, produced during combustion and used in various industrial processes.'),
    ('Nitrous Oxide', 'N2O', 'A colorless gas often used as a dental anesthetic and as a propellant in whipped cream dispensers.'),
    ('Phosphoric Acid', 'H3PO4', 'A weak acid used in the production of fertilizers and soft drinks.'),
    ('Ethylene Glycol', 'C2H6O2', 'A colorless, sweet-tasting liquid used as antifreeze and in the manufacture of plastics.'),
    ('Chloroform', 'CHCl3', 'A colorless, sweet-smelling liquid used as a solvent and anesthetic.'),
    ('Acetone', 'C3H6O', 'A colorless liquid solvent commonly used in nail polish removers and as an industrial solvent.'),
    ('Formaldehyde', 'CH2O', 'A colorless gas used as a preservative and in the manufacture of resins and plastics.'),
    # Continue with more compounds as needed...
]
compounds_data += [
    ('Nitric Acid', 'HNO3', 'A strong acid used in the production of fertilizers and explosives.'),
    ('Ammonium Nitrate', 'NH4NO3', 'A white crystalline salt used as a fertilizer and in explosives.'),
    ('Sodium Hydroxide', 'NaOH', 'A strong base and caustic substance used in cleaning and manufacturing.'),
    ('Phosphorus Pentoxide', 'P4O10', 'A white powder used as a desiccant and dehydrating agent.'),
    ('Benzene', 'C6H6', 'A colorless liquid and aromatic hydrocarbon used in the production of plastics and chemicals.'),
    ('Propane', 'C3H8', 'A colorless gas commonly used as fuel for heating and cooking.'),
    ('Carbon Tetrachloride', 'CCl4', 'A colorless liquid used as a solvent and fire extinguishing agent.'),
    ('Sulfuric Acid', 'H2SO4', 'A highly corrosive and strong acid used in various industrial processes.'),
    ('Ethylene', 'C2H4', 'A colorless gas and hydrocarbon used in the production of plastics and chemicals.'),
    ('Potassium Hydroxide', 'KOH', 'A strong base used in soap and detergent manufacturing.'),
    # Continue with more compounds as needed...
]
compounds_data += [
    ('Sodium Carbonate', 'Na2CO3', 'Also known as soda ash or washing soda, used in cleaning and manufacturing.'),
    ('Ethylene Glycol', 'C2H4(OH)2', 'Used as antifreeze and in the manufacture of plastics.'),
    ('Potassium Permanganate', 'KMnO4', 'A purple crystalline compound used as an oxidizing agent and disinfectant.'),
    ('Hydrogen Peroxide', 'H2O2', 'A colorless liquid used as a disinfectant and bleaching agent.'),
    ('Sulfur Hexafluoride', 'SF6', 'A colorless, odorless gas used in electrical insulation and as a tracer gas in various applications.'),
    ('Nitrogen Dioxide', 'NO2', 'A reddish-brown gas produced by combustion and used in the production of nitric acid.'),
    ('Boric Acid', 'H3BO3', 'A white crystalline compound used as a mild antiseptic and insecticide.'),
    ('Carbon Disulfide', 'CS2', 'A colorless liquid used as a solvent and in the manufacture of rayon and cellophane.'),
    ('Hydrogen Cyanide', 'HCN', 'A colorless, highly toxic gas used in chemical synthesis and fumigation.'),
    # Continue with more compounds as needed...
]
compounds_data += [
    ('Acetaminophen', 'C8H9NO2', 'A common over-the-counter pain reliever and fever reducer.'),
    ('Ascorbic Acid', 'C6H8O6', 'A water-soluble vitamin essential for human health.'),
    ('Sucrose', 'C12H22O11', 'A disaccharide sugar commonly used as table sugar.'),
    ('Lactic Acid', 'C3H6O3', 'A weak organic acid produced during muscle contraction.'),
    ('Citric Acid', 'C6H8O7', 'A weak organic acid found in citrus fruits and used as a food preservative and flavor enhancer.'),
    ('Caffeine', 'C8H10N4O2', 'A natural stimulant found in coffee, tea, and some soft drinks.'),
    ('Salicylic Acid', 'C7H6O3', 'A colorless organic compound used in skincare products and as an analgesic.'),
    ('Hydrochloric Acid', 'HCl', 'A strong inorganic acid used in various industrial processes.'),
    ('Formic Acid', 'CH2O2', 'A colorless liquid used as a preservative and in the production of textiles and leather.'),
    ('Sodium Hydroxide', 'NaOH', 'A strong base and caustic substance used in cleaning and manufacturing.'),
    # Continue with more compounds as needed...
]
compounds_data += [
    ('Starch', 'C6H10O5', 'A carbohydrate commonly found in plants and used as a food source.'),
    ('Hydrogen Sulfide', 'H2S', 'A colorless gas with a strong odor, often found in natural gas.'),
    ('Nitric Oxide', 'NO', 'A colorless gas involved in various physiological processes.'),
    ('Sulfur Hexafluoride', 'SF6', 'A colorless, odorless gas used in electrical insulation and as a tracer gas in various applications.'),
    ('Ammonium Nitrate', 'NH4NO3', 'A white crystalline salt used as a fertilizer and in explosives.'),
    ('Ethylene Oxide', 'C2H4O', 'A colorless gas used in sterilization and the production of various chemicals.'),
    ('Silicon Dioxide', 'SiO2', 'A compound commonly found in nature as quartz and used in various applications.'),
    ('Potassium Carbonate', 'K2CO3', 'A white salt used in the production of glass, soap, and other chemicals.'),
    ('Acetone', 'C3H6O', 'A colorless liquid solvent commonly used in nail polish removers and as an industrial solvent.'),
    # Continue with more compounds as needed...
]
for compound in compounds_data:
    if compound[0] not in compounds:
        name = compound[0]
        formula = compound[1]
        description = compound[2]
        insert_compound(name,formula,description)
        print(name)
        compounds.append(name)