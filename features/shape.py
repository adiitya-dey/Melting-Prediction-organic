from rdkit.Chem.Descriptors3D import Eccentricity, SpherocityIndex
from rdkit.Chem.GraphDescriptors import BalabanJ
from rdkit.Chem import Lipinski


class Shape:

    def __call__(self, mol):
        shape = {
            'ECCENTRICITY': Eccentricity(mol),
            'SPHERICITY': SpherocityIndex(mol),
            'BALABAN J': BalabanJ(mol),
            'ROTATABLE BONDS': Lipinski.NumRotatableBonds(mol)
        }
        return shape
