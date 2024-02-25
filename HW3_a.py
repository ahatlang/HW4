import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    # Define parameters for the two normal distributions
    mu1 = 0
    sigma1 = 1  # Mean and standard deviation for the first normal distribution

    mu2 = 175
    sigma2 = 3  # Mean and standard deviation for the second normal distribution

    # Create a range of x values for the first normal distribution
    x1 = np.linspace(-10, 10, 1000)

    # Create a range of x values for the second normal distribution
    x2 = np.linspace(150, 200, 1000)

    # Calculate the probability density function (pdf) for the first normal distribution
    pdf1 = stats.norm.pdf(x1, mu1, sigma1)

    cdf1 = stats.norm.cdf(x1, mu1, sigma1)

    # Calculate the probability density function (pdf) for the second normal distribution
    pdf2 = stats.norm.pdf(x2, mu2, sigma2)

    cdf2 = stats.norm.cdf(x2, mu2, sigma2)

    # Create a figure and two subplots for the first normal distribution
    fig, ax = plt.subplots(2, 1, figsize=(8, 10))

    # Plot the PDF of the first normal distribution on the first subplot
    ax[0].plot(x1, pdf1, label='N(0, 1)')
    ax[0].set_title('PDF of N(0, 1)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density')
    ax[0].legend()

    # Plot the CDF of the first normal distribution on the second subplot
    ax[1].plot(x1, cdf1, label='N(0, 1)')
    ax[1].set_title('CDF of N(0, 1)')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Probability')
    ax[1].legend()

    # Adjust layout and display the plot for the first normal distribution
    plt.tight_layout()
    plt.show()

    # Create a figure and two subplots for the second normal distribution
    fig, ax = plt.subplots(2, 1, figsize=(8, 10))

    # Plot the PDF of the second normal distribution on the first subplot
    ax[0].plot(x2, pdf2, label='N(175, 3)')
    ax[0].set_title('PDF of N(175, 3)')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Probability Density')
    ax[0].legend()

    # Plot the CDF of the second normal distribution on the second subplot
    ax[1].plot(x2, cdf2, label='N(175, 3)')
    ax[1].set_title('CDF of N(175, 3)')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Cumulative Probability')
    ax[1].legend()

    # Adjust layout and display the plot for the second normal distribution
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


