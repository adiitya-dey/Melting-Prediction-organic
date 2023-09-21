from rdkit import Chem


class BondCount:

    def __call__(self, mol):
        molecule = Chem.RemoveAllHs(mol)
        bonds = {
            'SINGLE BOND': self.single_bond_count(molecule),
            'DOUBLE BOND': self.double_bond_count(molecule),
            'TRIPLE BOND': self.triple_bond_count(molecule),
            'AROMATIC BOND': self.aromatic_bond_count(molecule)
        }

        return bonds

    # Total number of single bonds
    @staticmethod
    def single_bond_count(molecule):

        count_single = 0
        for atomic_bond in list(molecule.GetBonds()):
            bond = str(atomic_bond.GetBondType())
            if bond == "SINGLE":
                count_single += 1

        return count_single

    # Total number of double bonds
    @staticmethod
    def double_bond_count(molecule):

        count_double = 0
        for atomic_bond in list(molecule.GetBonds()):
            bond = str(atomic_bond.GetBondType())
            if bond == "DOUBLE":
                count_double += 1

        return count_double

    # Total number of triple bonds
    @staticmethod
    def triple_bond_count(molecule):

        count_triple = 0
        for atomic_bond in list(molecule.GetBonds()):
            bond = str(atomic_bond.GetBondType())
            if bond == "TRIPLE":
                count_triple += 1

        return count_triple

    # Total number of aromatic bonds
    @staticmethod
    def aromatic_bond_count(molecule):

        count_aromatic = 0
        for atomic_bond in list(molecule.GetBonds()):
            bond = str(atomic_bond.GetBondType())
            if bond == "AROMATIC":
                count_aromatic += 1

        return count_aromatic
