from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem import AllChem


class Density:

    def __call__(self, molecule):
        mol_wt = MolWt(molecule)
        volume = AllChem.ComputeMolVolume(molecule)
        density_params = {
            "MOL WEIGHT": mol_wt,
            "VOLUME": volume,
            "DENSITY": mol_wt / volume
        }
        return density_params
