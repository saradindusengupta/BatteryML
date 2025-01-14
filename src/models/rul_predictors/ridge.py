# Licensed under the MIT License.
# Copyright (c) Microsoft Corporation.

from sklearn.linear_model import Ridge

from src.builders import MODELS
from src.models.sklearn_model import SklearnModel


@MODELS.register()
class RidgeRULPredictor(SklearnModel):
    def __init__(self, *args, workspace: str = None, **kwargs):
        SklearnModel.__init__(self, workspace)
        self.model = Ridge(**kwargs)
