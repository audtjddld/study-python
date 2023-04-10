import pandas as pd
import sys
import os


def main(argv):
    fileName = argv[1]
    if fileName is None:
        print("file name is null")
        sys.exit(2)
    if ".xlsx" not in fileName:
        print("check file format .xlsx")
        sys.exit(2)

    # xlsx file 읽기
    xlsx_file = pd.read_excel(fileName)

    # convert csv file
    csvFileName = fileName.replace(".xlsx", ".csv")
    xlsx_file.to_csv(csvFileName, index=False)

    # convert csv file to tsv file
    readCsvFile = pd.read_csv(csvFileName, sep=',', engine='python', encoding='utf-8')

    readCsvFile.dropna(axis=0)
    # convert ',' to '\t' and save as tsv file
    tsvFileName = csvFileName.replace(".csv", ".tsv")
    readCsvFile.to_csv(tsvFileName, sep='\t', encoding='utf-8', index=False)
    print("conversion from '" + fileName + "' to '" + fileName.replace(".xlsx", ".tsv") + "' complete")
    # 종료

    # csv file 삭제
    if os.path.isfile(csvFileName):
        os.remove(csvFileName)
        # print("csv file 제거")
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
