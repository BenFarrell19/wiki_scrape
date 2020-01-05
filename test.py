from selenium import webdriver
import os, pandas as pd

num_of_elements = 36


browser = webdriver.Chrome(executable_path=os.path.abspath("../coursera/chromedriver.exe"))

elements = range(1,37)
element_lst = []
for i in elements:
    element_lst.append(i)


# ionization energies
browser.get('https://en.wikipedia.org/wiki/Ionization_energies_of_the_elements_(data_page)')
ion_c = 0
ion_elst = []
while ion_c < 4*num_of_elements:
    ion_c += 4
    ion_search = browser.find_elements_by_css_selector(
        '#mw-content-text > div > table > tbody > tr:nth-child({}) > td:nth-child(2)'.format(ion_c))
    ion_elst.append(ion_search)

ion_lst = []
for i in ion_elst:
    ion_lst.append(i[0].text)

# Electronegativity of elements
browser.get('https://en.wikipedia.org/wiki/Electronegativities_of_the_elements_(data_page)')
elec_c = 0
elec_elst = []
while elec_c < num_of_elements:
    elec_c += 1
    elec_search = browser.find_elements_by_css_selector(
        '#mw-content-text > div > table:nth-child(6) > tbody > tr:nth-child({}) > td:nth-child(4)'.format(elec_c))
    elec_elst.append(elec_search)

elec_lst = []
for i in elec_elst:
    elec_lst.append(i[0].text)

# Atomic Radii
browser.get('https://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page)')
radii_c = 0
radii_elst = []
while radii_c < num_of_elements:
    radii_c += 1
    radii_search = browser.find_elements_by_css_selector(
        '#mw-content-text > div > table > tbody > tr:nth-child({}) > td:nth-child(7) > a'.format(radii_c))
    radii_elst.append(radii_search)

radii_lst = []
for i in radii_elst:
    radii_lst.append(i[0].text)


# mass of elements
browser.get('https://www.cs.colorado.edu/~kena/classes/7818/f01/assignments/pt.html')
mass_c = 1
mass_elst = []
while mass_c < num_of_elements:
    mass_c += 1
    mass_search = browser.find_elements_by_css_selector(
        'body > table > tbody > tr:nth-child({}) > td:nth-child(2)'.format(mass_c))
    mass_elst.append(mass_search)

mass_lst = []
for i in mass_elst:
    mass_lst.append(i[0].text)


# boiling point
browser.get('https://www.cs.colorado.edu/~kena/classes/7818/f01/assignments/pt.html')
bp_c = 1
bp_elst = []

while bp_c < num_of_elements:
    bp_c += 1
    bp_search = browser.find_elements_by_css_selector(
        'body > table > tbody > tr:nth-child({}) > td:nth-child(4)'.format(bp_c))
    bp_elst.append(bp_search)

bp_lst = []
for i in bp_elst:
    bp_lst.append(i[0].text.strip(" Kelvin"))



# Density of elements

browser.get('https://en.wikipedia.org/wiki/Talk%3AList_of_elements_by_density/Numeric_densities')
dens_c = 0
dens_elst = []
while dens_c < 118:
    dens_c += 1
    dens_search = browser.find_elements_by_css_selector(
        '#mw-content-text > div > table.wikitable.sortable.jquery-tablesorter > tbody > tr:nth-child({}) > td:nth-child(3) > span'.format(dens_c))
    dens_elst.append(dens_search)

dens_lst = []
for i in dens_elst:
    dens_lst.append(i[0].text)

browser.get('https://en.wikipedia.org/wiki/Talk%3AList_of_elements_by_density/Numeric_densities')
n_dens_c = 0
n_dens_elst = []
while n_dens_c < 118:
    n_dens_c += 1
    n_dens_search = browser.find_elements_by_css_selector(
        '#mw-content-text > div > table.wikitable.sortable.jquery-tablesorter > tbody > tr:nth-child({}) > td:nth-child(5)'.format(n_dens_c))
    n_dens_elst.append(n_dens_search)

n_dens_lst = ['1']
count = 0
for i in n_dens_elst:
    count += 1
    try:
        n_dens_lst.append(i[0].text)
    except:
        print(i)
        continue

dct = {'values': dens_lst, 'num': n_dens_lst}

dens_df = pd.DataFrame(dct).sort_values('num').head(36)


# creating dictionary of collected data
data = {
    'Elements': element_lst,
    'Electronegativity': elec_lst,
    'Ionization Energy': ion_lst,
    'Atomic Radii': radii_lst,
    'Atomic Mass': mass_lst,
    'Boiling Point': bp_lst,
    'densities': dens_df
    }


#df = pd.DataFrame(data)

print(len(element_lst), len(elec_lst), len(ion_lst), len(radii_lst), len(mass_lst), len(bp_lst))
