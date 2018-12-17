#!/usr/bin/python
#coding:utf-8

import argparse

def main():
    parser = argparse.ArgumentParser(description = 'arg test')
    parser.add_argument('-s',help='Single song download')
    parser.add_argument('-c','--cd',help='CD download',action='store_true')
    args = parser.parse_args()

    if args.s:
        print(args.s)

    if args.cd == True:
        print('go')


if __name__ == "__main__":
    main()