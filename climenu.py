import argparse

from predictor import DepthEstimationModel


def main():
    parser = argparse.ArgumentParser(description="Depth Estimation with ZoeDepth")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument("output_path", type=str, help="Path to save the output image")
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depth_map(args.image_path, args.output_path)
    print(result)


if __name__ == "__main__":
    main()
