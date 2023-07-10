# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Configuration files for evaluation and visualization."""

import dataclasses
import typing as t
from typing import Dict

from weatherbench2.derived_variables import DerivedVariable
from weatherbench2.metrics import Metric
from weatherbench2.regions import ExtraTropicalRegion, LandRegion, Region, SliceRegion  # pylint: disable=g-multiple-import


@dataclasses.dataclass
class Selection:
  """Select a sub-set of data fields."""

  variables: t.Sequence[str]
  time_slice: slice
  levels: t.Optional[t.Sequence[int]] = None
  lat_slice: t.Optional[slice] = dataclasses.field(
      default_factory=lambda: slice(None, None)
  )
  lon_slice: t.Optional[slice] = dataclasses.field(
      default_factory=lambda: slice(None, None)
  )


@dataclasses.dataclass
class Paths:
  """Configuration for where to load and save data."""

  forecast: str
  obs: str
  output_dir: str
  output_file_prefix: t.Optional[str] = ''
  climatology: t.Optional[str] = None


@dataclasses.dataclass
class DataConfig:
  """Data configuration class."""

  selection: Selection
  paths: Paths
  by_init: t.Optional[bool] = False
  rename_variables: t.Optional[dict[str, str]] = None
  pressure_level_suffixes: t.Optional[bool] = False


@dataclasses.dataclass
class EvalConfig:
  """Evaluation configuration class."""

  metrics: t.Dict[str, Metric]
  regions: t.Optional[
      t.Dict[
          str, t.Union[Region, ExtraTropicalRegion, SliceRegion, LandRegion]
      ]
  ] = None
  evaluate_persistence: t.Optional[bool] = False
  evaluate_climatology: t.Optional[bool] = False
  evaluate_probabilistic_climatology: t.Optional[bool] = False
  probabilistic_climatology_start_year: t.Optional[int] = None
  probabilistic_climatology_end_year: t.Optional[int] = None
  probabilistic_climatology_hour_interval: t.Optional[int] = None
  against_analysis: t.Optional[bool] = False
  derived_variables: list[DerivedVariable] = dataclasses.field(
      default_factory=list
  )
  temporal_mean: t.Optional[bool] = True


@dataclasses.dataclass
class VizConfig:
  """Visualization configuration class."""

  results: t.Dict[str, str]
  save_kwargs: t.Dict[str, t.Any] = dataclasses.field(default_factory=dict)
  colors: t.Optional[t.Dict[str, str]] = None
  layout: t.Optional[t.Tuple[int, int]] = None
  figsize: t.Optional[t.Tuple[int, int]] = None
  tight_layout: t.Optional[bool] = True
  labels: t.Optional[t.Dict[str, str]] = None
  linestyles: t.Optional[t.Dict[str, str]] = None
  marker: t.Optional[str] = None
  markersize: t.Optional[int] = None


@dataclasses.dataclass
class PanelConfig:
  """Config for each panel."""

  metric: str
  variable: str
  level: t.Optional[int] = None
  region: t.Optional[str] = None
  relative: t.Optional[str] = None
  title: t.Optional[str] = None
  xlabel: t.Optional[str] = None
  ylabel: t.Optional[str] = None
  ylim: t.Optional[tuple[str]] = None
  xlim: t.Optional[tuple[str]] = None
