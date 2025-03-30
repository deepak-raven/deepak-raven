import github_contribution_grid as gcg

# Generate the 3D contribution heatmap
gcg.generate(
    username="deepak-raven",  # Replace with your GitHub username
    output_path="contribution-heatmap.svg",
    theme="dark",  # Options: light, dark, blue, red, etc.
    three_d=True   # Enable 3D effect
)
