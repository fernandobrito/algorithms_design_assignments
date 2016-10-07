class TestRunner:
    def __init__(self, function):
        self.function = function

    def expect_equal(self, input, expected):
        output = self.function(input)

        if  output != expected:
            raise ValueError('Test error. Expected {}. Returned: {}.'.format(expected, output))

        print('.', end="")