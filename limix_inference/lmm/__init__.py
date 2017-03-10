r"""
*******************
Linear Mixed Models
*******************

Introduction
^^^^^^^^^^^^

A LMM can be described as

.. math::

    \mathbf y = \mathrm M\boldsymbol\beta + \mathbf u + \boldsymbol\epsilon

where :math:`\mathbf u \sim \mathcal N(\mathbf 0, \mathrm K)` and
:math:`\epsilon_i` are iid Normal random variables.
This module provides two methods for fitting LMMs via maximum
likelihood: :class:`.SlowLMM` and :class:`.FastLMM`.
The former is more general but slower then the later;
the later one assumes a scaled covariance matrix.

Public interface
^^^^^^^^^^^^^^^^
"""

from .fastlmm import FastLMM, NormalLikTrick
from .slowlmm import SlowLMM

__all__ = ['SlowLMM', 'FastLMM', 'NormalLikTrick']
