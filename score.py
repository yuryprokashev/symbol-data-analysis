def adf_score(symbol_adf_result):
    """
    Gives the 1 point, when adf test statistics value is negative, 0 otherwise
    Adds 1 point, when adf test statistics value is below 10% threshold
    Adds 1 point, when adf test statistics value is below 5% threshold
    Adds 1 point, when adf test statistics value is below 1% threshold
    So minimum score is 0, maximum score is 4.
    Notice that since we expect mean regression, λ/SE(λ) has to be negative,
    and it has to be more negative than the critical value for the hypothesis to
    be rejected.
    @param symbol_adf_result:
    @return:
    """
    score = 0
    adf_statistics = symbol_adf_result[2]
    adf_statistics_value = adf_statistics[0]
    threshold_10 = adf_statistics[4]["10%"]
    threshold_5 = adf_statistics[4]["5%"]
    threshold_1 = adf_statistics[4]["1%"]
    if adf_statistics_value < 0:
        score += 1
    if adf_statistics_value < threshold_10:
        score += 1
    if adf_statistics_value < threshold_5:
        score += 1
    if adf_statistics_value < threshold_1:
        score += 1
    return symbol_adf_result[0], symbol_adf_result[1], score


def hurst_score(symbol_hurst_result):
    """
    Gives 1 when hurst exponent is less than 1, 0 otherwise
    Adds 1 when hurst exponent is less than 0.5
    @param symbol_hurst_result:
    @return:
    """
    score = 0
    message = "H is above 1"
    hurst_exponent = symbol_hurst_result[2][0]
    if hurst_exponent < 1:
        score += 1
        message = "trending"
    if hurst_exponent < 0.5:
        score += 1
        message = "mean-reverting"
    return symbol_hurst_result[0], symbol_hurst_result[1], score, message
