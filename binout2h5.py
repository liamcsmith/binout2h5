import argparse
import sys
import os


def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(description='Convert binout to h5')
    parser.add_argument('input',
                        help='Path to the input binout.')
    parser.add_argument('--output',
                        help='Path to output folder.')
    return parser


def ImpBinout(input, output="./"):
    from lasso.dyna import Binout
    if os.path.exists(os.path.dirname(output)):
        if str.endswith(output, ".h5"):
            Binout(input).save_hdf5(output)
        else:
            Binout(input).save_hdf5(
                os.path.join(output, "binouthdf5.h5"))
        return


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.input):
        ImpBinout(parsed_args.input,
                  parsed_args.output)
