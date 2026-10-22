"""Generate a small publication-style line chart."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from publication_figures import OKABE_ITO, set_publication_style


def main() -> None:
    size = set_publication_style("nature_single")
    output_dir = Path(__file__).resolve().parents[1] / "figures" / "drafts"
    output_dir.mkdir(parents=True, exist_ok=True)

    x = np.arange(1, 6)
    control = np.array([1.0, 1.4, 1.7, 2.0, 2.2])
    treatment = np.array([1.0, 1.7, 2.4, 3.0, 3.5])

    fig, ax = plt.subplots(figsize=size, constrained_layout=True)
    ax.plot(x, control, marker="o", label="Control", color=OKABE_ITO["blue"])
    ax.plot(
        x,
        treatment,
        marker="s",
        linestyle="--",
        label="Treatment",
        color=OKABE_ITO["vermillion"],
    )
    ax.set(xlabel="Time (day)", ylabel="Response (a.u.)")
    ax.legend(frameon=False)

    for suffix in ("pdf", "png"):
        fig.savefig(output_dir / f"demo_figure.{suffix}")
    plt.close(fig)


if __name__ == "__main__":
    main()
