#importsregion
import random
import math
#endregion

#functionsregion
def gen_rock_size(mean, variance):  #reusing function from ex1a
    """
    Step 1: generate a single rock size from a normal distribution given the mean and variance.
    :param mean: mean of the size of the rocks.
    :param variance: variance in the sizes of the rocks.
    :return: float representing the size of a rock.
    """
    return random.gauss(mean, math.sqrt(variance))

def gen_sample(sample_size, mean, variance):  #reusing function from ex1a
    """
    Step 2: generate a sample of rock sizes using normal distribution.
    :param sample_size: number of rocks in the sample.
    :param mean: mean size of the rocks
    :param variance: variance in the sizes of the rocks.
    :return: list of rock sizes for the sample.
    """
    return [gen_rock_size(mean, variance) for _ in range(sample_size)]

def calc_mean(sample):  #reusing function from ex1a
    """
    Step 3: calculate the mean of the sample.
    :param sample: list of rock sizes.
    :return: mean size of the rocks in the sample.
    """
    return sum(sample) / len(sample)

def calc_variance(sample, sample_mean):  #reusing function from ex1a
    """
    Step 4: calculates the variance of the sample.
    :param sample: list of rock sizes.
    :param sample_mean: mean size of the rocks in the sample.
    :return: variance of the rock sizes in the sample.
    """
    return sum((x - sample_mean) ** 2 for x in sample) / (len(sample) - 1)

def calc_std_dev(variance):
    """
    Step 5: calculate the standard deviation from variance.
    :param: variance: variance of sample
    :return: standard deviation of the sample
    """
    return math.sqrt(variance)

def perform_t_test(mean_a, mean_b, std_dev_a, std_dev_b, n_a, n_b):
    """
    Step 6: perform a one-sided t-test to compare two means.
    :param mean_a: mean of sample A
    :param mean_b: mean of sample B
    :param std_dev_a: standard deviation of sample A
    :param std_dev_b: standard deviation of sample B
    :param n_a: sample size of sample A
    :param n_b: sample size of sample B
    :return: t-statistics and degrees of freedom
    """
    #chatgpt was used for this function
    #calculate pooled standard deviation
    pooled_std_dev = math.sqrt(((n_a - 1) * std_dev_a ** 2 + (n_b - 1) * std_dev_b ** 2) / (n_a + n_b - 2))
    #calculate standard error
    se = pooled_std_dev * math.sqrt(1/n_a + 1/n_b)
    #calculate t-statistic
    t_stat = (mean_a - mean_b) / se
    #degrees of freedom
    df = n_a + n_b - 2
    return t_stat, df
#endregion

#inputregion
supplier_a_sample = gen_sample(30, 10, 2)  # Adjust mean and variance as needed
supplier_b_sample = gen_sample(30, 8, 2)   # Adjust mean and variance for Supplier B
#endregion

#calcregion
"""
Calculate statistic based off input samples
"""
mean_a = calc_mean(supplier_a_sample)
mean_b = calc_mean(supplier_b_sample)
variance_a = calc_variance(supplier_a_sample, mean_a)
variance_b = calc_variance(supplier_b_sample, mean_b)
std_dev_a = calc_std_dev(variance_a)
std_dev_b = calc_std_dev(variance_b)
n_a = len(supplier_a_sample)
n_b = len(supplier_b_sample)

#perform one-sided t-test chatgpt was used here
t_stat, df = perform_t_test(mean_a, mean_b, std_dev_a, std_dev_b, n_a, n_b)

#assuming a critical t-value from a t-distribution table based on df and α = 0.05 for a one-sided test
critical_t_value = 1.645  #assumption value for a one-sided test with high degrees of freedom
#endregion

#printregion
print(f"Mean of Supplier A: {mean_a:.2f}")
print(f"Mean of Supplier B: {mean_b:.2f}")
print(f"T-statistic: {t_stat:.2f}")
print(f"Degrees of freedom: {df}")
print(f"Critical t-value for α = 0.95: {critical_t_value}")

if t_stat > critical_t_value:
    print("Reject the null hypothesis: Supplier B's gravel size is statistically significantly smaller than Supplier A's at α = 0.95.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to conclude that Supplier B's gravel size is significantly smaller than Supplier A's at α = 0.95.")
#endregion


