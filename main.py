import sys

_DASH = '-'
_DOT = '.'
_BAR = '|'
_WELCOME = 'WELCOME'
_PATTERN = f'{_DOT}{_BAR}{_DOT}'


def main(unused_argv):
    height, width = map(int, sys.stdin.readline().split())

    welcome_line = [f'{_WELCOME}'.center(width, '-')]
    top_pattern = [(_PATTERN*(2 * i + 1)).center(width, '-') for i in range(height//2)]
    bottom_pattern = top_pattern[::-1]
    print('\n'.join(top_pattern + welcome_line + bottom_pattern))


if __name__ == '__main__':
    main(sys.argv)