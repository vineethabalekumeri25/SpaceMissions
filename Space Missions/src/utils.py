def save_summary_to_file(summary, output_path):
    """
    Save analysis summary to a text file.
    """
    with open(output_path, 'w') as file:
        file.write(summary)
    print(f"Summary saved at {output_path}")