# Zoe Depth Estimation

This project is a Python-based application that uses the ZoeDepth model from the [isl-org](https://github.com/isl-org/ZoeDepth) repository for depth estimation in images.

## Usage/Examples

### CLI Usage

```bash
usage: climenu.py [-h] input_image output_image

Depth Estimation with ZoeDepth

positional arguments:
    input_image     Path to input image.
    output_image    Path to output depth map.
options:
    -h, --help      show this help message and exit

```

### API Usage

```
http://127.0.0.1:8064/predict
```

## Installation

Install DepthEstimation with pip

```bash
pip install -r requirements.txt
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`IMAGE_API_KEY`

## Deployment

To deploy this project run

```bash
  docker build -t depth_estimation .
  docker run -d -p 8064:8064 depth_estimation
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
