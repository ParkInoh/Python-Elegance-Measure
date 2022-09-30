import constants
import elegance
import PythonCodeAnalyzer
import eleganceUtils
import json
import argparse
import numpy as np

import utils


def main():
    # 커맨드라인 옵션 추가
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ignore', dest='usr_ignore', nargs='+', default=None, required=False)
    parser.add_argument('-l', '--max_line_length', dest='usr_max_line_length', type=int, default=200, required=False)
    parser.add_argument('-v', '--violation', dest='usr_violation', default='', required=False)
    args = parser.parse_args()

    # 파일, 코드 리스트
    files = eleganceUtils.get_files_by_dir()  # list[str]
    files = [file for file in files if file.endswith('.py')]  # list[str]
    codes = eleganceUtils.get_codes(files)  # list[str]

    # region Elegance
    # 객체 인스턴스 생성
    if args.usr_ignore is None:
        args.ignore = constants.IGNORE
    instance = elegance.Elegance(args.ignore, args.usr_max_line_length)

    # region PEP8 위반 검사
    print('\nfile check:')
    reports = instance.get_PEP8_metrics(files)
    PEP8_violations = [[[violation.split()[1], violation.split()[0]] for violation in report]
                       for report in reports if len(reports) > 0]
    PEP8_violation_counts = [len(report) for report in reports]
    z_PEP8_violations = utils.get_z_scores(PEP8_violation_counts)
    # endregion

    # region 순환복잡도 검사
    depths = instance.get_cyclomatic_metrics(codes)
    max_depths = [max(depth) if len(depth) > 0 else 0 for depth in depths]
    avg_depths = [sum(depth) / len(depth) if len(depth) > 0 else 0 for depth in depths]
    sum_depths = [sum(depth) if len(depth) > 0 else 0 for depth in depths]
    z_max_depths = utils.get_z_scores(max_depths)
    z_avg_depths = utils.get_z_scores(avg_depths)
    z_sum_depths = utils.get_z_scores(sum_depths)
    # endregion

    # region PythonCodeAnalyzer
    # json 파일을 생성함
    analyzer_result = {}

    conditionals_all = []
    loops_all = []
    functions_all = []
    recursions_all = []

    scores = []

    for file_name, code in zip(files, codes):
        analyzer = PythonCodeAnalyzer.PythonDepthBreadth()
        analyzer.analyze_python_code(code)

        # conditional
        conditionals = analyzer.print_conditional()
        conditionals_all.append(len(conditionals))

        # loop
        loop = analyzer.print_loop()
        loops_all.append(len(loop))

        # functions
        analyzer2 = PythonCodeAnalyzer.PythonDepthBreadth()
        analyzer2.analyze_python_function(code)
        functions = analyzer2.print_function()
        functions_all.append(len(functions))

        # recursion
        recursion_count = 0
        for element in functions:
            if element[2] == True:
                recursion_count += 1
        recursions_all.append(recursion_count)

    z_conditionals = utils.get_z_scores(conditionals_all)
    z_loops = utils.get_z_scores(loops_all)
    z_functions = utils.get_z_scores(functions_all)
    z_recursions = utils.get_z_scores(recursions_all)
    # endregion

    # region 점수 계산 및 파일 출력
    for i in range(len(files)):
        score = 0 - (z_max_depths[i] + z_sum_depths[i] + z_PEP8_violations[i]
                     + z_recursions[i] + z_functions[i] + z_loops[i] + z_conditionals[i])
        scores.append(score)

    for file_name, score, conditionals, loops, functions, recursions, z_max_depth, z_avg_depth, z_sum_depth \
            in zip(files, scores, conditionals_all, loops_all, functions_all, recursions_all, z_max_depths, z_avg_depths, z_sum_depths):
        # 출력부
        json_obj = {
            "score": round(score, 3),
            "conditionals": conditionals,
            "loops": loops,
            "functions": functions,
            "functions_recursion": recursions,
            "max_depth": z_max_depth,
            "avg_depth": z_avg_depth,
            "sum_depth": z_sum_depth,
        }
        # add file to analyzer_result with json_obj
        analyzer_result[file_name] = json_obj

    with open('output.json', 'w') as f:
        json.dump(analyzer_result, f, indent=4)
    # endregion


if __name__ == '__main__':
    main()
