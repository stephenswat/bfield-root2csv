import argparse
import uproot
import pathlib
import csv
import tqdm


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        type=pathlib.Path,
        help="ROOT file to use as input",
    )
    parser.add_argument(
        "dir",
        help="ROOT directory to read from in input file",
        type=str,
    )
    parser.add_argument(
        "output",
        type=pathlib.Path,
        help="CSV file to use as output",
    )

    args = parser.parse_args()

    with uproot.open(args.input) as ifile:
        with open(args.output, "w") as ofile:
            writer = csv.DictWriter(ofile, fieldnames=["x", "y", "z", "Bx", "By", "Bz"])

            writer.writeheader()

            for i in tqdm.tqdm(ifile[args.dir].arrays(["x", "y", "z", "Bx", "By", "Bz"])):
                writer.writerow({"x": i["x"], "y": i["y"], "z": i["z"], "Bx": i["Bx"], "By": i["By"], "Bz": i["Bz"]})
