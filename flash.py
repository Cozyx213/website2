import requests
from bs4 import BeautifulSoup
import sqlite3

def insert_flashcard(element_name, element_symbol, atomic_number, other_info=''):
    
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO flashcards (element_name, element_symbol, atomic_number, other_info)
        VALUES (?, ?, ?, ?)
    ''', (element_name, element_symbol, atomic_number, other_info))
    
    
    conn.commit()
    conn.close()

# Example flashcard insertion
#insert_flashcard('Hydrogen', 'H', 1, 'The lightest element in the universe.')

# Create the flashcards table if it doesn't exist


# Example: Scrape and insert data for Hydrogen


elements_data = [
    ('Hydrogen', 'H', 1, 'The lightest element in the universe.'),
    ('Helium', 'He', 2, 'The second lightest element and noble gas.'),
    ('Lithium', 'Li', 3, 'A soft, silver-white metal.'),
    ('Beryllium', 'Be', 4, 'An alkaline earth metal with a gray-white appearance.'),
    ('Boron', 'B', 5, 'A metalloid element with a brown amorphous powder appearance.'),
    ('Carbon', 'C', 6, 'A fundamental element for life, occurring in a variety of forms.'),
    ('Nitrogen', 'N', 7, 'A colorless, odorless diatomic gas.'),
    ('Oxygen', 'O', 8, 'A reactive nonmetal and essential for combustion.'),
    ('Fluorine', 'F', 9, 'A pale yellow diatomic gas.'),
    ('Neon', 'Ne', 10, 'A noble gas known for its bright red-orange glow in neon signs.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Sodium', 'Na', 11, 'A soft, silvery-white alkali metal.'),
    ('Magnesium', 'Mg', 12, 'An alkaline earth metal with a gray appearance.'),
    ('Aluminum', 'Al', 13, 'A lightweight and corrosion-resistant metal.'),
    ('Silicon', 'Si', 14, 'A metalloid with various industrial applications.'),
    ('Phosphorus', 'P', 15, 'A nonmetal that exists in several allotropic forms.'),
    ('Sulfur', 'S', 16, 'A multivalent nonmetal with distinctive odor.'),
    ('Chlorine', 'Cl', 17, 'A pale green diatomic gas.'),
    ('Argon', 'Ar', 18, 'A noble gas used in various applications.'),
    ('Potassium', 'K', 19, 'A soft, silvery-white alkali metal.'),
    ('Calcium', 'Ca', 20, 'An alkaline earth metal with a gray appearance.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Scandium', 'Sc', 21, 'A transition metal with a silvery-white appearance.'),
    ('Titanium', 'Ti', 22, 'A strong and lightweight transition metal.'),
    ('Vanadium', 'V', 23, 'A transition metal with a silver-gray appearance.'),
    ('Chromium', 'Cr', 24, 'A shiny, hard, and brittle transition metal.'),
    ('Manganese', 'Mn', 25, 'A transition metal often found in ores.'),
    ('Iron', 'Fe', 26, 'A metal essential for various biological processes.'),
    ('Cobalt', 'Co', 27, 'A hard, brittle, and magnetic transition metal.'),
    ('Nickel', 'Ni', 28, 'A silvery-white and lustrous transition metal.'),
    ('Copper', 'Cu', 29, 'A ductile and malleable transition metal with a reddish-orange hue.'),
    ('Zinc', 'Zn', 30, 'A bluish-white and corrosion-resistant transition metal.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Gallium', 'Ga', 31, 'A soft, silvery-blue metal with a low melting point.'),
    ('Germanium', 'Ge', 32, 'A metalloid used in semiconductors.'),
    ('Arsenic', 'As', 33, 'A metalloid known for its toxicity.'),
    ('Selenium', 'Se', 34, 'A nonmetal with essential biological functions.'),
    ('Bromine', 'Br', 35, 'A dark red-brown liquid at room temperature.'),
    ('Krypton', 'Kr', 36, 'A noble gas used in lighting and lasers.'),
    ('Rubidium', 'Rb', 37, 'A soft, silvery-white alkali metal.'),
    ('Strontium', 'Sr', 38, 'An alkaline earth metal used in fireworks.'),
    ('Yttrium', 'Y', 39, 'A transition metal often used in alloys.'),
    ('Zirconium', 'Zr', 40, 'A lustrous and corrosion-resistant transition metal.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Niobium', 'Nb', 41, 'A transition metal often used in superconductors.'),
    ('Molybdenum', 'Mo', 42, 'A transition metal with high melting and boiling points.'),
    ('Technetium', 'Tc', 43, 'A radioactive element with no stable isotopes.'),
    ('Ruthenium', 'Ru', 44, 'A rare transition metal known for its corrosion resistance.'),
    ('Rhodium', 'Rh', 45, 'A rare and expensive transition metal.'),
    ('Palladium', 'Pd', 46, 'A transition metal used in catalytic converters.'),
    ('Silver', 'Ag', 47, 'A precious metal known for its luster and conductivity.'),
    ('Cadmium', 'Cd', 48, 'A soft, bluish-white metal often used in batteries.'),
    ('Indium', 'In', 49, 'A post-transition metal with a silvery-white appearance.'),
    ('Tin', 'Sn', 50, 'A post-transition metal known for its malleability and low melting point.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Antimony', 'Sb', 51, 'A metalloid with a bluish-white appearance and toxic properties.'),
    ('Tellurium', 'Te', 52, 'A metalloid with semiconducting properties.'),
    ('Iodine', 'I', 53, 'A dark purple-black solid at room temperature.'),
    ('Xenon', 'Xe', 54, 'A noble gas used in lighting and anesthesia.'),
    ('Cesium', 'Cs', 55, 'A soft, silvery-gold alkali metal.'),
    ('Barium', 'Ba', 56, 'An alkaline earth metal with a pale green color.'),
    ('Lanthanum', 'La', 57, 'A rare-earth metal used in various applications.'),
    ('Cerium', 'Ce', 58, 'A rare-earth metal often used in catalysts.'),
    ('Praseodymium', 'Pr', 59, 'A rare-earth metal with a bright, silvery finish.'),
    ('Neodymium', 'Nd', 60, 'A rare-earth metal used in strong magnets and lasers.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Promethium', 'Pm', 61, 'A radioactive rare-earth metal.'),
    ('Samarium', 'Sm', 62, 'A rare-earth metal used in magnets and nuclear reactors.'),
    ('Europium', 'Eu', 63, 'A rare-earth metal used in phosphorescent materials.'),
    ('Gadolinium', 'Gd', 64, 'A rare-earth metal with magnetic properties.'),
    ('Terbium', 'Tb', 65, 'A rare-earth metal used in fluorescent lamps.'),
    ('Dysprosium', 'Dy', 66, 'A rare-earth metal used in magnets and lasers.'),
    ('Holmium', 'Ho', 67, 'A rare-earth metal used in nuclear control rods.'),
    ('Erbium', 'Er', 68, 'A rare-earth metal used in fiber optics and lasers.'),
    ('Thulium', 'Tm', 69, 'A rare-earth metal often used in portable X-ray machines.'),
    ('Ytterbium', 'Yb', 70, 'A rare-earth metal used in lasers and atomic clocks.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Lutetium', 'Lu', 71, 'A rare-earth metal used in radiation therapy.'),
    ('Hafnium', 'Hf', 72, 'A transition metal used in nuclear reactors.'),
    ('Tantalum', 'Ta', 73, 'A transition metal known for its high melting point.'),
    ('Tungsten', 'W', 74, 'A dense, high-melting-point transition metal.'),
    ('Rhenium', 'Re', 75, 'A rare and dense transition metal.'),
    ('Osmium', 'Os', 76, 'A dense, brittle, and rare transition metal.'),
    ('Iridium', 'Ir', 77, 'A dense, corrosion-resistant transition metal.'),
    ('Platinum', 'Pt', 78, 'A precious metal known for its luster and catalytic properties.'),
    ('Gold', 'Au', 79, 'A precious metal with a distinctive yellow color.'),
    ('Mercury', 'Hg', 80, 'A silvery-white, liquid transition metal.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Thallium', 'Tl', 81, 'A soft, bluish-gray metal with toxic properties.'),
    ('Lead', 'Pb', 82, 'A heavy metal with a bluish-white appearance.'),
    ('Bismuth', 'Bi', 83, 'A post-transition metal known for its distinctive appearance.'),
    ('Polonium', 'Po', 84, 'A radioactive element with no stable isotopes.'),
    ('Astatine', 'At', 85, 'A highly radioactive halogen.'),
    ('Radon', 'Rn', 86, 'A radioactive noble gas.'),
    ('Francium', 'Fr', 87, 'A highly radioactive alkali metal.'),
    ('Radium', 'Ra', 88, 'A radioactive alkaline earth metal.'),
    ('Actinium', 'Ac', 89, 'A radioactive actinide metal.'),
    ('Thorium', 'Th', 90, 'A radioactive actinide often used in nuclear reactors.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Protactinium', 'Pa', 91, 'A radioactive actinide metal.'),
    ('Uranium', 'U', 92, 'A radioactive actinide often used in nuclear reactors and weapons.'),
    ('Neptunium', 'Np', 93, 'A radioactive actinide metal, used in the early development of nuclear reactors.'),
    ('Plutonium', 'Pu', 94, 'A radioactive actinide often used in nuclear weapons and reactors.'),
    ('Americium', 'Am', 95, 'A radioactive actinide used in smoke detectors and nuclear devices.'),
    ('Curium', 'Cm', 96, 'A radioactive actinide used in research and industry.'),
    ('Berkelium', 'Bk', 97, 'A radioactive actinide, part of the transuranium element series.'),
    ('Californium', 'Cf', 98, 'A radioactive actinide, used in neutron sources.'),
    ('Einsteinium', 'Es', 99, 'A synthetic radioactive element, named after Albert Einstein.'),
    ('Fermium', 'Fm', 100, 'A synthetic radioactive element, named after Enrico Fermi.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Mendelevium', 'Md', 101, 'A synthetic radioactive element, named after Dmitri Mendeleev.'),
    ('Nobelium', 'No', 102, 'A synthetic radioactive element, named after Alfred Nobel.'),
    ('Lawrencium', 'Lr', 103, 'A synthetic radioactive element, named after Ernest O. Lawrence.'),
    ('Rutherfordium', 'Rf', 104, 'A synthetic radioactive element, named after Ernest Rutherford.'),
    ('Dubnium', 'Db', 105, 'A synthetic radioactive element, named after the city of Dubna, Russia.'),
    ('Seaborgium', 'Sg', 106, 'A synthetic radioactive element, named after Glenn T. Seaborg.'),
    ('Bohrium', 'Bh', 107, 'A synthetic radioactive element, named after Niels Bohr.'),
    ('Hassium', 'Hs', 108, 'A synthetic radioactive element, named after the Latin name for the German state of Hesse.'),
    ('Meitnerium', 'Mt', 109, 'A synthetic radioactive element, named after Lise Meitner.'),
    ('Darmstadtium', 'Ds', 110, 'A synthetic radioactive element, named after the city of Darmstadt, Germany.'),
    # Continue with more elements as needed...
]
elements_data += [
    ('Roentgenium', 'Rg', 111, 'A synthetic radioactive element, named after Wilhelm Conrad Roentgen.'),
    ('Copernicium', 'Cn', 112, 'A synthetic element, named after Nicolaus Copernicus.'),
    ('Nihonium', 'Nh', 113, 'A synthetic element, named after Nihon, the Japanese name for Japan.'),
    ('Flerovium', 'Fl', 114, 'A synthetic element, named after Flerov Laboratory of Nuclear Reactions.'),
    ('Moscovium', 'Mc', 115, 'A synthetic element, named after Moscow Oblast, Russia.'),
    ('Livermorium', 'Lv', 116, 'A synthetic element, named after Lawrence Livermore National Laboratory.'),
    ('Tennessine', 'Ts', 117, 'A synthetic element, named after the state of Tennessee.'),
    ('Oganesson', 'Og', 118, 'A synthetic element, named after Yuri Oganessian.'),
]

for element in elements_data:
    insert_flashcard(element[0],element[1],element[2],element[3])
    
# You've now covered all the known elements up to Oganesson (Element 118).
