import argparse
from itertools import product

color_print = lambda text: print("\33[48;5;34m" + text + "\33[0m")


def calc(modulo: int):
    for p, q in product(list(range(modulo)), repeat=2):
        res = p * p - 2 * q * q
        res_modulo = res % modulo
        text = f"({p=:<2},{q=:<2})  {p}\N{SUPERSCRIPT TWO}-2*{q}\N{SUPERSCRIPT TWO} = {res:>3} = ({res_modulo} mod {modulo})"

        color_print(text) if res_modulo == 0 else print(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--modulo", help="Modulo", required=True, type=int)
    args = parser.parse_args()

    calc(args.modulo)
