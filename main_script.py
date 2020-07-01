import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description='specify inputs')
    parser.add_argument('-p', '--path', type=str, help='specify .db database path', required=True)
    parser.add_argument('-c', '--country', type = str, help = 'specify country...', dest='country')
    args = parser.parse_args()
    return args


def main(args):
    print('starting pipeline...')
    print('Getting the data from database...')
    raw_data = mac.acquire(args.path)
    print('Data from database is there!...')
    print('Dealing with data...')
    data = mwr.wrangling(raw_data)
    print('Data dealt!')
    print('analysing the data...')
    molins = man.analysis(data, args.country)
    print(molins)
    print('Data analysed!...')

    # mre.report(top_return_risk_companies, returns_corr)

    print('========================= Pipeline is complete. You may find the results in the folder '
          './data/results =========================')



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)