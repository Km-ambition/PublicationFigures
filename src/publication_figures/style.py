"""Shared matplotlib settings for publication-ready figures."""

from __future__ import annotations

from typing import Literal

import matplotlib.pyplot as plt


FIGURE_SIZES = {
    "nature_single": (3.5, 2.625),
    "nature_double": (7.2, 5.4),
    "ieee_single": (3.5, 2.5),
    "ieee_double": (7.16, 5.0),
    "general": (5.0, 3.5),
}

OKABE_ITO = {
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "bluish_green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "reddish_purple": "#CC79A7",
    "black": "#000000",
}


def set_publication_style(
    preset: str = "general",
    language: Literal["en", "zh"] = "en",
) -> tuple[float, float]:
    """Apply a compact, vector-friendly matplotlib style.

    Args:
        preset: One of the keys in ``FIGURE_SIZES``.
        language: ``zh`` adds common CJK font fallbacks.

    Returns:
        The selected final figure size in inches.
    """
    if preset not in FIGURE_SIZES:
        choices = ", ".join(sorted(FIGURE_SIZES))
        raise ValueError(f"Unknown preset {preset!r}; choose one of: {choices}")

    if language not in {"en", "zh"}:
        raise ValueError("language must be 'en' or 'zh'")

    size = FIGURE_SIZES[preset]
    sans_fonts = ["Arial", "Helvetica", "DejaVu Sans"]
    if language == "zh":
        sans_fonts = [
            "Noto Sans CJK SC",
            "Source Han Sans SC",
            "Microsoft YaHei",
            "SimHei",
            *sans_fonts,
        ]

    plt.rcParams.update(
        {
            "figure.figsize": size,
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "font.family": "sans-serif",
            "font.sans-serif": sans_fonts,
            "font.size": 8,
            "axes.labelsize": 8,
            "axes.titlesize": 9,
            "axes.linewidth": 0.7,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.unicode_minus": False,
            "xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "legend.fontsize": 7,
            "lines.linewidth": 1.2,
            "lines.markersize": 4,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )
    return size
