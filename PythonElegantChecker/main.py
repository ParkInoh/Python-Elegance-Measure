import constants
import elegance
import PythonCodeAnalyzer
import eleganceUtils
import json
import argparse
import numpy as np


def main():
    # 커맨드라인 옵션 추가
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ignore', dest='usr_ignore', nargs='+', default='', required=False)
    parser.add_argument('-l', '--max_line_length', dest='usr_max_line_length', type=int, default=200, required=False)
    parser.add_argument('-v', '--violation', dest='usr_violation', default='', required=False)
    args = parser.parse_args()

    # 파일, 코드 리스트
    files = eleganceUtils.get_files_by_dir()  # list[str]
    files = [file for file in files if file.endswith('.py')]  # list[str]
    codes = eleganceUtils.get_codes(files)  # list[str]

    # region Elegance
    # 객체 인스턴스 생성
    if args.usr_ignore == '':
        args.ignore = constants.IGNORE
    instance = elegance.Elegance(args.ignore, args.usr_max_line_length)

    # region PEP8 위반 검사
    print('\nfile check:')
    reports = instance.get_PEP8_metrics(files)
    PEP8_violations = [[[violation.split()[1], violation.split()[0]] for violation in report]
                       for report in reports if len(reports) > 0]
    # PEP8_violation_counts = [len(report) for report in reports]
    # print('PEP8 violations(ALL):', reports)
    print('PEP8 violations:', PEP8_violations)
    # print('PEP8 violation counts:', PEP8_violation_counts)
    # endregion

    # region 순환복잡도 검사
    print('\ncode check:')
    depths = instance.get_cyclomatic_metrics(codes)
    # halstead = instance.get_halstead_metrics(codes)
    # halstead = [[round(halstead[i][j], 2) for j in range(len(halstead[i]))] for i in range(len(halstead))]
    max_depths = [max(depth) if len(depth) > 0 else 0 for depth in depths]
    avg_depths = [sum(depth) / len(depth) if len(depth) > 0 else 0 for depth in depths]
    sum_depths = [sum(depth) if len(depth) > 0 else 0 for depth in depths]
    std_max_depth = np.std(max_depths)
    std_avg_depth = np.std(avg_depths)
    std_sum_depth = np.std(sum_depths)
    mean_max_depth = np.mean(max_depths)
    mean_avg_depth = np.mean(avg_depths)
    mean_sum_depth = np.mean(sum_depths)
    z_max_depths = [round((depth - mean_max_depth) / std_max_depth, 3) for depth in max_depths]
    z_avg_depths = [round((depth - mean_avg_depth) / std_avg_depth, 3) for depth in avg_depths]
    z_sum_depths = [round((depth - mean_sum_depth) / std_sum_depth, 3) for depth in sum_depths]
    # raw_metrics = elegance.get_raw_metrics(codes)
    # endregion

    # region 결과 출력
    # print('depths:', depths)
    # print('max depths:', max_depths)
    # print('avg depths:', avg_depths)
    # print('sum depths:', sum_depths)
    # print('max depths:', z_max_depths)
    # print('avg depths:', z_avg_depths)
    # print('sum depths:', z_sum_depths)
    # print('halstead:', halstead)
    # print('raw metrics:', raw_metrics)
    # endregion

    # region Variable Name Check
    # # check for variable names
    # print('\nvariable name check:')
    # # test tokens
    # tokens = ['test', 'apple', 'aaa', 'aaba', 'ab', 'aa', 'x', 'a']
    # violations = instance.check_name_correctness(tokens)
    # print('tokens:', tokens)
    # print('violations:', violations)
    # violation_counts = violations.count(True)
    # print('name violation counts:', violation_counts)
    # endregion
    # endregion

    # region PythonCodeAnalyzer
    # json 파일을 생성함
    analyzer_result = {}

    for file_name, code, max_depth, avg_depth, sum_depth in zip(files, codes, z_max_depths, z_avg_depths, z_sum_depths):
        analyzer = PythonCodeAnalyzer.PythonDepthBreadth()
        analyzer.analyze_python_code(code)

        # conditional
        conditionals = analyzer.print_conditional()

        # loop
        loop = analyzer.print_loop()
        for_count = 0
        for element in loop:
            if element[0][:3] == 'for':
                for_count += 1
        while_count = len(loop) - for_count

        # functions
        analyzer2 = PythonCodeAnalyzer.PythonDepthBreadth()
        analyzer2.analyze_python_function(code)
        functions = analyzer2.print_function()

        # recursion
        recursion_count = 0
        for element in functions:
            if element[2] == True:
                recursion_count += 1

        # 출력부
        json_obj = {
            "conditionals": len(conditionals),
            "loops": len(loop),
            "loops_for": for_count,
            "loops_while": while_count,
            "functions": len(functions),
            "functions_recursion": recursion_count,
            "max_depth": max_depth,
            "avg_depth": avg_depth,
            "sum_depth": sum_depth
        }
        # add file to analyzer_result with json_obj
        analyzer_result[file_name.split('.')[0]] = json_obj

        # print(fileName)
        # print('conditional(if):', len(conditionals))
        #
        # #print('loop:', loop)
        # print('loop:', len(loop))
        # print('loop(for):', for_count)
        # print('loop(while):', while_count)
        #
        # #print('functions:', functions)
        # print('functions:', len(functions))
        # print('recursions:', recursion_count)

    with open('output.json', 'w') as f:
        json.dump(analyzer_result, f, indent=4)
    # endregion


if __name__ == '__main__':
    main()
