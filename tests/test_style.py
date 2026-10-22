import matplotlib.pyplot as plt
import pytest

from publication_figures import FIGURE_SIZES, OKABE_ITO, set_publication_style


def test_nature_single_style() -> None:
    size = set_publication_style("nature_single")

    assert size == FIGURE_SIZES["nature_single"]
    assert plt.rcParams["pdf.fonttype"] == 42
    assert OKABE_ITO["blue"] == "#0072B2"


def test_unknown_preset_is_rejected() -> None:
    with pytest.raises(ValueError, match="Unknown preset"):
        set_publication_style("unknown")
