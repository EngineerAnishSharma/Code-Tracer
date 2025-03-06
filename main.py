from wrapper import stepbystep_wrapper

@stepbystep_wrapper(time_between_steps=1)
def sample_function():
    x = 10
    y = 20
    z = x + y
    print("Result:", z)

sample_function()
