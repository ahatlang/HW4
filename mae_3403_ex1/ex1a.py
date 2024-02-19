#importsregion
import random
import math
#endregion

#functionsregion
def gen_rock_size(mean, variance):
    """
    Step 1: generate a single rock size from a normal distribution given the mean and variance.
    :param mean: mean of the size of the rocks.
    :param variance: variance in the sizes of the rocks.
    :return: float representing the size of a rock.
    """
    return random.gauss(mean, math.sqrt(variance))  #chatgpt was used in this function

def gen_sample(sample_size, mean, variance):
    """
    Step 2: generate a sample of rock sizes using normal distribution.
    :param sample_size: number of rocks in the sample.
    :param mean: mean size of the rocks
    :param variance: variance in the sizes of the rocks.
    :return: list of rock sizes for the sample.
    """
    return [gen_rock_size(mean, variance) for _ in range(sample_size)]

def calc_mean(sample):
    """
    Step 3: calculate the mean of the sample.
    :param sample: list of rock sizes.
    :return: mean size of the rocks in the sample.
    """
    return sum(sample) / len(sample)

def calc_variance(sample, sample_mean):
    """
    Step 4: calculates the variance of the sample.
    :param sample: list of rock sizes.
    :param sample_mean: mean size of the rocks in the sample.
    :return: variance of the rock sizes in the sample.
    """
    return sum((x - sample_mean) ** 2 for x in sample) / len(sample)

def simulate_rock_crushing(operation_samples, sample_size, mean, variance):
    """
    Step 5: simulate a rock crushing operation, generating multiple samples and calculating the means and variances
    :param operation_samples: number of samples to generate.
    :param sample_size: number of rocks in each sample.
    :param mean: assumed mean size of the rocks.
    :param variance: assumed variance in the sizes of the rocks.
    """
    #chatgpt was used in this function
    sample_means = []
    sample_variances = []

    for _ in range(operation_samples):
        sample = gen_sample(sample_size, mean, variance)
        sample_mean = calc_mean(sample)
        sample_variance = calc_variance(sample, sample_mean)

        sample_means.append(sample_mean)
        sample_variances.append(sample_variance)

        print(f"Sample Mean: {sample_mean}, Sample Variance: {sample_variance}")

    overall_mean = calc_mean(sample_means)
    overall_variance = calc_variance(sample_means, overall_mean)
#endregion

#printregion
    print(f"Mean of Sampling Means: {overall_mean}, Variance of Sampling Means: {overall_variance}")


#given numbers to plug into program
simulate_rock_crushing(11, 100, 5, 1.5)
#endregion
