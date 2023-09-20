from rdkit.Chem import Fragments


class FragmentCount:
    
    def __call__(self, mol):
        
        fragment_count = {
        "fr_Al_OH": Fragments.fr_Al_OH(mol), # R-OH
        "fr_Ar_COO": Fragments.fr_Ar_COO(mol),  # Ar-COOH
        "fr_Al_COO": Fragments.fr_Al_COO(mol),  # R-COOH
        "fr_Ar_OH": Fragments.fr_Ar_OH(mol),  # Ar-OH
        "fr_aldehyde": Fragments.fr_aldehyde(mol),  # R-CHO
        "fr_benzene": Fragments.fr_benzene(mol), # Benzene Rings
        "fr_Ar_N": Fragments.fr_Ar_N(mol),  # Aromatic Nitrogens
        "fr_Ar_NH":Fragments.fr_Ar_NH(mol),  # Aromatic amines
        "fr_Imine": Fragments.fr_Imine(mol),  # Imines
        "fr_NH0": Fragments.fr_NH0(mol),  # (R)(R)(R)N
        "fr_NH1": Fragments.fr_NH1(mol),  # (R)(R)NH
        "fr_NH2": Fragments.fr_NH2(mol), # (R)NH2
        "fr_N_O": Fragments.fr_N_O(mol),  # hydroxyl amines
        "fr_imidazole": Fragments.fr_imidazole(mol),
        "fr_isocyan": Fragments.fr_isocyan(mol),
        "fr_ketone": Fragments.fr_ketone(mol),
        "fr_lactone": Fragments.fr_lactone(mol),
        "fr_methoxy": Fragments.fr_methoxy(mol),
        "fr_morpholine": Fragments.fr_morpholine(mol),
        "fr_nitrile": Fragments.fr_nitrile(mol),
        "fr_nitro": Fragments.fr_nitro(mol),
        "fr_nitro_arom": Fragments.fr_nitro_arom(mol),
        "fr_nitroso": Fragments.fr_nitroso(mol),
        "fr_oxazole": Fragments.fr_oxazole(mol),
        "fr_oxime": Fragments.fr_oxime(mol),
        "fr_phenol": Fragments.fr_phenol(mol),
        "fr_phos_acid": Fragments.fr_phos_acid(mol),
        "fr_phos_ester": Fragments.fr_phos_ester(mol),
        "fr_piperdine": Fragments.fr_piperdine(mol),
        "fr_piperzine": Fragments.fr_piperzine(mol),
        "fr_priamide": Fragments.fr_priamide(mol),
        "fr_prisulfonamd": Fragments.fr_prisulfonamd(mol),
        "fr_pyridine": Fragments.fr_pyridine(mol),
        "fr_sulfide": Fragments.fr_sulfide(mol),
        "fr_sulfonamd": Fragments.fr_sulfonamd(mol),
        "fr_sulfone": Fragments.fr_sulfone(mol),
        "fr_term_acetylene": Fragments.fr_term_acetylene(mol),
        "fr_tetrazole": Fragments.fr_tetrazole(mol),
        "fr_thiazole": Fragments.fr_thiazole(mol),
        "fr_thiocyan": Fragments.fr_thiocyan(mol),
        "fr_thiophene": Fragments.fr_thiophene(mol),
        "fr_unbrch_alkane": Fragments.fr_unbrch_alkane(mol),
        "fr_urea": Fragments.fr_urea(mol),
        "fr_C_S": Fragments.fr_C_S(mol),  # Thio carbonyl
        "fr_SH": Fragments.fr_SH(mol),  # R-SH
        "fr_alkyl_carbamate": Fragments.fr_alkyl_carbamate(mol),  # Alkyl Carbamates
        "fr_alkyl_halide": Fragments.fr_alkyl_halide(mol),  # R-X
        "fr_aryl_methyl": Fragments.fr_aryl_methyl(mol),  # Benzene-(CH3)
        "fr_amide": Fragments.fr_amide(mol),
        "fr_amidine": Fragments.fr_amidine(mol),
        "fr_aniline": Fragments.fr_aniline(mol),
        "fr_azide": Fragments.fr_azide(mol),  # Use it for Validation.
        "fr_azo": Fragments.fr_azo(mol),  # R-N=N-R'
        "fr_barbitur": Fragments.fr_barbitur(mol),
        "fr_bicyclic": Fragments.fr_bicyclic(mol),
        "fr_epoxide": Fragments.fr_epoxide(mol),
        "fr_ester": Fragments.fr_ester(mol),
        "fr_ether": Fragments.fr_ether(mol),
        "fr_furan": Fragments.fr_furan(mol),
        "fr_guanido": Fragments.fr_guanido(mol),
        "fr_hdrzone": Fragments.fr_hdrzone(mol), # (R)(R)C=N-NH2
        "fr_hdrzine": Fragments.fr_hdrzine(mol),  # (R)(R)N-N(R)(R)
        "fr_Ndealkylation1": Fragments.fr_Ndealkylation1(mol),  # XCCNR group --> **Confusing**
        "fr_Ndealkylation2": Fragments.fr_Ndealkylation2(mol),
            # tert-alicyclic amines (no heteroatoms, not quinine-like bridged N)
        "fr_HOCCN": Fragments.fr_HOCCN(mol),  # C(OH)CCN
        "fr_Nhpyrrole": Fragments.fr_Nhpyrrole(mol),  # H-pyrrole nitrogens --> Isn't it similar to aromatic nitrogens ?
        
        }

        return fragment_count

