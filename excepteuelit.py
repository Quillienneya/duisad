def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

my_function(a=1, b=2, c=3)
