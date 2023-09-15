import sqlite3

def insert_compound(compound_name, chemical_formula, description, charge):
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO ions(element_name, element_symbol, other_info, charge)
        VALUES (?, ?, ?,? )
    ''', (compound_name, chemical_formula, description, charge))

    conn.commit()
    conn.close()
ions = [
    ("Hydrogen ion", "H^+", 1, "This is simply a lone proton."),
    ("Sodium ion", "Na^+", 1, "Formed when sodium (Na) loses one electron."),
    ("Potassium ion", "K^+", 1, "Formed when potassium (K) loses one electron."),
    ("Magnesium ion", "Mg^2+", 2, "Formed when magnesium (Mg) loses two electrons."),
    ("Calcium ion", "Ca^2+", 2, "Formed when calcium (Ca) loses two electrons."),
    ("Iron(II) ion (Ferrous ion)", "Fe^2+", 2, "Formed when iron (Fe) loses two electrons."),
    ("Iron(III) ion (Ferric ion)", "Fe^3+", 3, "Formed when iron (Fe) loses three electrons."),
    ("Copper(I) ion (Cuprous ion)", "Cu^+", 1, "Formed when copper (Cu) loses one electron."),
    ("Copper(II) ion (Cupric ion)", "Cu^2+", 2, "Formed when copper (Cu) loses two electrons."),
    ("Hydride ion", "H^-", -1, "Formed when hydrogen (H) gains one electron."),
    ("Fluoride ion", "F^-", -1, "Formed when fluorine (F) gains one electron."),
    ("Chloride ion", "Cl^-", -1, "Formed when chlorine (Cl) gains one electron."),
    ("Bromide ion", "Br^-", -1, "Formed when bromine (Br) gains one electron."),
    ("Iodide ion", "I^-", -1, "Formed when iodine (I) gains one electron."),
    ("Oxide ion", "O^2-", -2, "Formed when oxygen (O) gains two electrons."),
    ("Sulfide ion", "S^2-", -2, "Formed when sulfur (S) gains two electrons."),
    ("Nitride ion", "N^3-", -3, "Formed when nitrogen (N) gains three electrons.")
]
for i in ions:
    name = i[0]
    formula = i[1]
    charge = i[2]
    description = i[3]
    insert_compound(name, formula, description, charge)

