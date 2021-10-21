"""
    ██████  ███████  ██████  ██████  ██████   █████  ████████  ██████  ██████  ███████
    ██   ██ ██      ██      ██    ██ ██   ██ ██   ██    ██    ██    ██ ██   ██ ██
    ██   ██ █████   ██      ██    ██ ██████  ███████    ██    ██    ██ ██████  ███████
    ██   ██ ██      ██      ██    ██ ██   ██ ██   ██    ██    ██    ██ ██   ██      ██
    ██████  ███████  ██████  ██████  ██   ██ ██   ██    ██     ██████  ██   ██ ███████
"""

# Q: what's the first encounter with decorators when learning Python? #






##
import sys


class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value + 1

obj = MyClass(2)
print(obj.value)



##
def control_airplane_speed(speed: float) -> None:
    """our control function"""
    print(f"flying at {speed} m/s")


control_airplane_speed(4.0)


##
control_airplane_speed("?")


##
def robust_control_airplane_speed(speed: float) -> None:
    """our control function"""
    if not isinstance(speed, (float, int)):
        print(f"ERROR: got {speed} falling back to 4.0")
        speed = 4.0
    print(f"flying at {speed} m/s")


robust_control_airplane_speed("?")
robust_control_airplane_speed({})
robust_control_airplane_speed([])



##
from typing import Callable
# What if we need this in multiple different control functions?
# I would tell you:
# >> go through the code and add this check to each function

def add_fallback_on_bad_input(
    control_function: Callable[[float], None]
) -> Callable[[float], None]:
    # ???
    return fixed_control_function



##
def add_fallback_on_bad_input(control_function):

    def fixed_control_function(speed):
        if not isinstance(speed, float):
            print(f"ERROR: got {speed} falling back to 4.0")
            speed = 4.0
        return control_function(speed)

    return fixed_control_function

f0 = control_airplane_speed
f1 = add_fallback_on_bad_input(control_airplane_speed)

f0([])
f1([])


##

@add_fallback_on_bad_input
def control_car_speed(speed):
    print(f"driving at {speed} km/h")


control_car_speed(1.0)
control_car_speed("???")



##
# decorator syntax equivalent to

@add_fallback_on_bad_input
def func0(speed):
    ...

def func1(speed):
    ...
func1 = add_fallback_on_bad_input(func1)


##
# best practice
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...  # do something before
        value = func(*args, **kwargs)
        ...  # do something after
        return value
    return wrapper


@my_decorator
def abc():
    """print the ABC"""
    print("abc")


##
# let's do some wishful thinking programming
"""
@requires_range(0, 10)
def my_func(index):
    ...
"""

def requires_range(min_val, max_val):
    def decorator(func):
        @wraps(func)
        def wrapper(index):
            if not (min_val <= index <= max_val):
                raise ValueError("out of range")
            return func(index)
        return wrapper
    return decorator


@add_fallback_on_bad_input
@requires_range(2.0, 10.0)
def control_boat_speed(speed):
    """our boat speed"""
    print(f"floats at {speed} nautical miles / hour")


##
# logging example:

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"called {func.__name__} with {args!r} {kwargs!r}", file=sys.stderr)
        return func(*args, **kwargs)
    return wrapper

@log_call
def do_something(a, b):
    return a + b


##
# timing example
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.monotonic()
        val = func(*args, **kwargs)
        print(func.__name__, "took", time.monotonic() - t0, "seconds")
        return val
    return wrapper

@timer
def takes_a_bit():
    time.sleep(1.0)


##

def decorator(func: Callable) -> Any:
    ...
    return ...


##
#
from typing import Protocol
from typing import runtime_checkable

@runtime_checkable
class ControllerProtocol(Protocol):
    def set_target(self, target: float) -> None:
        ...
    def run(self) -> None:
        ...

def do_something(ctrl: ControllerProtocol) -> None:
    if not isinstance(ctrl, ControllerProtocol):
        raise TypeError("not a controller")
    ctrl.set_target(4.0)
    ctrl.run()


##
# === DECORATORS TAKE HOME MESSAGE ===

from functools import wraps

def my_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...  # do something before
        value = func(*args, **kwargs)
        ...  # do something after
        return value
    return wrapper
