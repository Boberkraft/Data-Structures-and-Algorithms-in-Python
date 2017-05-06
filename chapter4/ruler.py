def draw_line(tick_lenght, tick_label=''):
    line = '-' * tick_lenght
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_lenght):
    if center_lenght > 0:
        draw_interval(center_lenght-1)
        draw_line(center_lenght)
        draw_interval(center_lenght-1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))

if __name__ == '__main__':
    # draw_ruler(20,4)
    c = 2
    draw_interval(c)
    print(2**c-1)
    print(2**(c+1)-c-2)