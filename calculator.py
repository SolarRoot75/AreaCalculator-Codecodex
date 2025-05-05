import math
import time

def display_banner():
    banner = '''
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                                                                   ┃
    ┃     █▀█ █▀█ █▀▀ ▄▀█   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█     ┃
    ┃     █▀▄ █▀▀ ██▄ █▀█   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄     ┃
    ┃                                                                   ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    '''
    
    for line in banner.split('\n'):
        print(line)
        time.sleep(0.1)

def calculate_square_area():
    side = float(input('Enter a side length: '))
    return side ** 2

def calculate_rectangle_area():
    length = float(input('Enter a length: '))
    width = float(input('Enter a width: '))
    return length * width

def calculate_triangle_area():
    base = float(input('Enter a base: '))
    height = float(input('Enter a height: '))
    return (base * height) / 2

def calculate_circle_area():
    print(f'pi = {math.pi}')
    radius = float(input('Enter a radius: '))
    return math.pi * (radius ** 2)

def main():
    display_banner()
    
    print(
        '''
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃   📐  Q - Which surface equation would you like to use?  📐  ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
           
            1) Square
            2) Rectangle
            3) Triangle
            4) Circle
        '''
    )
    
    try:
        choice = int(input('Answer: '))
        
        if choice == 1:
            area = calculate_square_area()
            print(f'The area of the square is {area}.')
        elif choice == 2:
            area = calculate_rectangle_area()
            print(f'The area of the rectangle is {area}.')
        elif choice == 3:
            area = calculate_triangle_area()
            print(f'The area of the triangle is {area}.')
        elif choice == 4:
            area = calculate_circle_area()
            print(f'The area of the circle is {area}.')
        else:
            print('Invalid input. Please select a number between 1 and 4.')
    except ValueError:
        print('Please enter a valid number.')

if __name__ == "__main__":
    main()
