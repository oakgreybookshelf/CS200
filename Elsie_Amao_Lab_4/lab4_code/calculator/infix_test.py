from infix import evaluate_infix

def test_evaluate_None_is_error():
    try:
        evaluate_infix(None)
        assert False
    except Exception:
        assert True

def test_evaluate_empty_is_error():
    try:
        evaluate_infix('')
        assert False
    except Exception:
        assert True

def test_evaluate():
    test_cases = [
        ('2', 2),
        ('2+3', 5),
        ('2-3+4', 3),
        ('2-3*4', -10),
        ('2-3*4/6', 0),
        ('(2)', 2),
        ('2-(3+4)', -5),
        ('(2-3)*4', -4),
        ('((2-3)*4)/2', -2),
        ('3+4/2-6', -1)
    ]
    for postfix, expected in test_cases:
        result = evaluate_infix(postfix)
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