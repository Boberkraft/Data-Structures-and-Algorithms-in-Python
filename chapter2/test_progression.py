from progression import Progression
from geometricprogression import GeometricProgression
from fibonacciprogression import FibonacciProgression
from arithmeticprogression import ArithmeticProgression

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(10)

    print('Geometric progression wiht default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progession with base 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4,6).print_progression(10)