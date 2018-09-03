import matplotlib.pyplot as plt

def quality_to_probability(quality_seq):
    """Converts string of quality scores to array of probabilities"""
    probabilities = []

    for quality_score in quality_seq:
        quality_mapping = ord(quality_score) - 33
        probability = 10**(quality_mapping/-10)
        probabilities.append(round(probability, 8))
        
    return probabilities

def plot_array(array, modifier = "b"):
    plt.plot(range(len(array)), array, modifier)
    plt.axis([0, len(array), min(array), max(array)])
    plt.show
    
    




