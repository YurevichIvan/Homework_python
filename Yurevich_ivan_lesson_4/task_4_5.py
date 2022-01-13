import argparse
from utils import currency_rates

parser = argparse.ArgumentParser()
parser.add_argument('code', type=str)
args = parser.parse_args()
print(currency_rates(args.code))

# читал как это сделать в гугле, вроде все как там написано, но выдает ошибку:
#usage: task_4_5.py [-h] code
#task_4_5.py: error: the following arguments are required: code