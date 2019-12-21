from collections import defaultdict


def run(data):
    pixels = [int(p) for p in data]
    rows, cols = 6, 25

    layer_pixels = rows * cols

    assert len(pixels) % layer_pixels == 0

    zero_counts = defaultdict(int)
    for i, pixel in enumerate(pixels):
        if pixel == 0:
            zero_counts[i // layer_pixels] += 1

    most_zeros_layer = min(zero_counts.keys(), key=lambda k: zero_counts[k])
    most_zeros_layer = pixels[layer_pixels * most_zeros_layer:layer_pixels * (most_zeros_layer + 1)]
    return len([p for p in most_zeros_layer if p == 1]) * len([p for p in most_zeros_layer if p == 2])
