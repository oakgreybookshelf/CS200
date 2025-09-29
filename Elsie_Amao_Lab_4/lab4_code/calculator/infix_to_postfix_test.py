from infix_to_postfix import infix_to_postfix

def test_infix_to_postfix_None_is_error():
    try:
        infix_to_postfix(None)
        assert False # should not get here
    except Exception:
        assert True

def test_infix_to_postfix():
    test_cases = [
        ('', ''),
        ('2', '2'),
        ('2+3', '23+'),
        ('2-3+4', '23-4+'),
        ('2-3*4', '234*-'),
        ('2-3*4/6', '234*6/-'),
        ('(2)', '2'),
        ('2-(3+4)', '234+-'),
        ('(2-3)*4', '23-4*'),
        ('((2-3)*4)/2', '23-4*2/'),
        ('3+4/2-6', '342/+6-')
    ]
    for infix, postfix in test_cases:
        result = infix_to_postfix(infix)
        assert result == postfix , f'Failed: {infix=} {postfix=} {result=}'

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

test_functions = [test_infix_to_postfix_None_is_error, test_infix_to_postfix]
run_all_tests(test_functions)