def run(data):
    pixels = [int(p) for p in data]
    rows, cols = 6, 25
    pixels_per_layer = rows * cols
    assert len(pixels) % pixels_per_layer == 0
    num_layers = len(pixels) // pixels_per_layer

    output = []
    for row_idx in range(rows):
        row_output = []
        for col_idx in range(cols):
            for layer_idx in range(num_layers):
                pixel = pixels[col_idx + row_idx * cols + layer_idx * pixels_per_layer]
                if pixel == 0 or pixel == 1:
                    row_output.append(pixel)
                    break

        output.append(row_output)

    return "\n".join("".join("X" if x == 0 else " " for x in row) for row in output)
