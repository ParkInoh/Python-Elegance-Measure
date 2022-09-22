import elegance
import PythonCodeAnalyzer
import utils
import json


def main():
    # 파일, 코드 리스트
    files = utils.get_files_by_dir()  # list[str]
    codes = utils.get_codes(files)  # list[str]

    # region Elegance
    # 객체 인스턴스 생성
    instance = elegance.Elegance()

    # region PEP8 위반 검사
    print('\nfile check:')
    reports = instance.get_PEP8_metrics(files)
    PEP8_violations = [[[violation.split()[1], violation.split()[0]] for violation in report] for report in reports if len(reports) > 0]
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
    avg_depths = [round(sum(depth) / len(depth), 2) if len(depth) > 0 else 0 for depth in depths]
    sum_depths = [sum(depth) if len(depth) > 0 else 0 for depth in depths]
    # raw_metrics = elegance.get_raw_metrics(codes)
    # endregion

    # region 결과 출력
    # print('depths:', depths)
    # print('max depths:', max_depths)
    # print('avg depths:', avg_depths)
    # print('sum depths:', sum_depths)
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
    analyzer_result = {}

    for file_name, code, max_depth, avg_depth, sum_depth \
            in zip(files, codes, max_depths, avg_depths, sum_depths):
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
        analyzer_result[file_name] = json_obj

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

    # json_object = json.dumps(analyzer_result)
    with open('output.json', 'w') as f:
        json.dump(analyzer_result, f, indent=4)
    # endregion


if __name__ == '__main__':
    main()
