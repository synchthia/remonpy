#!/usr/bin/env python3

Data = {
    "cool": {
        "temp": {
            "type": "RANGE",
            "default": 21,
            "range": {
                "step": 1,
                "from": 16,
                "to": 31
            }
        },
        "fan": {
            "type": "STEP",
            "default": "auto",
            "step": [
                "auto",
                "low",
                "mid",
                "high"
            ]
        },
        "vertical_vane": {
            "type": "STEP",
            "default": "auto",
            "step": [
                "auto",
                "1",
                "2",
                "3",
                "4",
                "5"
            ]
        },
        "horizontal_vane": {
            "type": "BUTTON",
            "default": "keep",
            "button": [
                "keep",
                "swing"
            ]
        }
    },
    "dry": {
        "temp": None,
        "fan": {
            "type": "STEP",
            "default": "auto",
            "step": [
                "auto"
            ]
        },
        "vertical_vane": {
            "type": "STEP",
            "default": "auto",
            "step": [
                "auto",
                "1",
                "2",
                "3",
                "4",
                "5"
            ]
        },
        "horizontal_vane": {
            "type": "BUTTON",
            "default": "keep",
            "button": [
                "keep",
                "swing"
            ]
        }
    },
    "heat": {
        "temp": {
            "type": "RANGE",
            "default": 27,
            "range": {
                "step": 1,
                "from": 16,
                "to": 31
            }
        },
        "fan": {
            "type": "STEP",
            "default": "auto",
            "step": [
                "auto",
                "low",
                "mid",
                "high"
            ]
        },
        "vertical_vane": {
            "type": "STEP",
            "default": "auto",
            "step": [
                "auto",
                "1",
                "2",
                "3",
                "4",
                "5"
            ]
        },
        "horizontal_vane": {
            "type": "BUTTON",
            "default": "keep",
            "button": [
                "keep",
                "swing"
            ]
        }
    }
}