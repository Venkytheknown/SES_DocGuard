# filepath: SES-DocGuard/src/viz/attention_viz.py
import matplotlib.pyplot as plt
import numpy as np
import json

def plot_attention_weights(attention_weights, layer_names, output_path):
    """
    Plots attention weights for each layer and saves the figure.

    Parameters:
    - attention_weights: List of attention weights for each layer.
    - layer_names: List of layer names corresponding to the attention weights.
    - output_path: Path to save the attention visualization.
    """
    num_layers = len(attention_weights)
    fig, axes = plt.subplots(num_layers, 1, figsize=(10, 2 * num_layers))

    for i, (weights, layer_name) in enumerate(zip(attention_weights, layer_names)):
        ax = axes[i]
        ax.matshow(weights, cmap='viridis')
        ax.set_title(f'Attention Weights - {layer_name}')
        ax.set_xlabel('Input Tokens')
        ax.set_ylabel('Output Tokens')
        plt.colorbar(ax.matshow(weights, cmap='viridis'), ax=ax)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def save_attention_maps(attention_maps, output_dir):
    """
    Saves attention maps to the specified directory.

    Parameters:
    - attention_maps: Dictionary containing attention maps for each run.
    - output_dir: Directory to save the attention maps.
    """
    for run_id, maps in attention_maps.items():
        output_path = f"{output_dir}/{run_id}_attention.png"
        plot_attention_weights(maps['weights'], maps['layer_names'], output_path)

def load_attention_maps(json_file):
    """
    Loads attention maps from a JSON file.

    Parameters:
    - json_file: Path to the JSON file containing attention maps.

    Returns:
    - attention_maps: Loaded attention maps.
    """
    with open(json_file, 'r') as file:
        attention_maps = json.load(file)
    return attention_maps

# Example usage (to be removed or commented out in production):
# if __name__ == "__main__":
#     attention_maps = load_attention_maps('path/to/attention_maps.json')
#     save_attention_maps(attention_maps, 'path/to/output_dir')