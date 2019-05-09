from dataclasses import dataclass, field
from typing import Dict
from django import forms

from marshmallow import Schema, fields, validate, exceptions
from paramtools import ValueValidatorSchema

from webapp.apps.comp.fields import coerce_bool


@dataclass
class MetaParameters:
    parameters: Dict[str, "MetaParameter"] = field(default_factory=dict)

    def validate(self, fields: dict) -> dict:
        validated = {}
        if not self.parameters:
            return validated
        for param_name, param_data in self.parameters.items():
            try:
                cleaned = param_data.field.clean(fields.get(param_name))
            except (forms.ValidationError, KeyError) as e:
                # fall back on default. deal with bad data in full validation.
                cleaned = param_data.field.clean(param_data.value)
            validated[param_name] = cleaned
        return validated


@dataclass
class MetaParameter:
    title: str
    description: str
    value: str
    field: forms.Field


def translate_to_django(meta_parameters: dict) -> MetaParameters:
    new_mp = {}
    for name, data in meta_parameters.items():
        if data["type"] == "str" and "choice" in data["validators"]:
            field = forms.ChoiceField(
                label="",
                choices=[(c, c) for c in data["validators"]["choice"]["choices"]],
            )
        elif data["type"] == "str":
            field = forms.CharField(label="")
        elif data["type"] in ("int", "float"):
            field = forms.IntegerField if data["type"] == "int" else forms.FloatField
            if "range" in data["validators"]:
                min_value = data["validators"]["range"]["min"]
                max_value = data["validators"]["range"]["max"]
                field = field(label="", min_value=min_value, max_value=max_value)
            else:
                field = field(label="")
        else:  # bool
            field = forms.TypedChoiceField(
                label="",
                coerce=coerce_bool,
                choices=list((i, i) for i in (True, False)),
            )
        if isinstance(data["value"], list):
            val = data["value"][0]["value"]
        else:
            val = data["value"]
        new_mp[name] = MetaParameter(
            title=data["title"], description=data["description"], value=val, field=field
        )
    return MetaParameters(parameters=new_mp)
