def single_variable_function_error_propagation(func, a, aerr, assymetric=True):
    """
    Parameters
    ----------
    func : function
        A function of a single variable.
    a : float
        The value of the variable.
    aerr : float
        The uncertainty in the variable.
    assymetric : bool, optional
        Whether the uncertainty in the variable is assymetric. The default is True.

    Returns
    -------
    float
        The uncertainty in the calculated value of the function.
    """

    calc_val = func(a)

    if assymetric:
        err_1 = func(a + aerr) - func(a)
        err_2 = func(a) - func(a - aerr)

        if err_1 > 0 and err_2 < 0:
            plus_err = err_1
            minus_err = err_2
        else:
            plus_err = err_2
            minus_err = err_1

        out = f"{calc_val} + {plus_err}, - {minus_err}"
    elif not assymetric:
        err = func(a + aerr) - func(a)
        out = f"{calc_val} +/- {err}"
    return out


test_func = lambda x: (10**x)
test1 = single_variable_function_error_propagation(test_func, 2.3, 0.1, assymetric=True)
print(test1)

test2 = single_variable_function_error_propagation(
    test_func, 2.3, 0.1, assymetric=False
)
print(test2)
