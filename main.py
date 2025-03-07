from wrapper import stepbystep_wrapper

@stepbystep_wrapper(time_between_steps=1)
def sample_function():
    arr = [64, 34, 25, 12, 22, 11, 90]

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted array is:", arr)

sample_function()
