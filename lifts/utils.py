from enum import IntEnum


class WorkoutTypes(IntEnum):
    FOR_TIME = "For Time"
    AMRAP = "AMRAP"
    EMOM = "EMOM"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
