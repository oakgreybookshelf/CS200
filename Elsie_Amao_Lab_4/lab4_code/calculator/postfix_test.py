from postfix import evaluate_postfix

def test_evaluate_None_is_error():
    try:
        evaluate_postfix(None)
        assert False
    except Exception:
        assert True

def test_evaluate_empty_is_error():
    try:
        evaluate_postfix('')
        assert False
    except Exception:
        assert True

def test_evaluate():
    test_cases = [
        ('2', 2),
        ('23+', 5),
        ('23-4+', 3),
        ('234*-', -10),
        ('234*6/-', 0),
        ('2', 2),
        ('234+-', -5),
        ('23-4*', -4),
        ('23-4*2/', -2),
        ('342/+6-', -1)
    ]
    for postfix, expected in test_cases:
        result = evaluate_postfix(postfix)
        assert result == expected , f'{postfix=} {expected=} {result=}'

def run_all_tests(function_list):
    import traceback
    
    for function in function_list:
        try:
            function()
            print('Passed test for', function.__name__)
        except AssertionError:
            print('Failed test for', function.__name__, '-- Assertion failed')
            print(traceback.format_exc())
        except Exception:
            print('Failed test for', function.__name__, '-- Another error occurred')
            print(traceback.format_exc())

test_functions = [test_evaluate_None_is_error, test_evaluate_empty_is_error, test_evaluate]
run_all_tests(test_functions)