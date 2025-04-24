#  Write a program to implement Midpoint ellipse drawing algorithm.
import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, points):
    # 4-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ])

def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    px = 0
    py = two_rx2 * y

    points = []

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    while px < py:
        plot_ellipse_points(xc, yc, x, y, points)
        x += 1
        px += two_ry2
        if p1 < 0:
            p1 += ry2 + px
        else:
            y -= 1
            py -= two_rx2
            p1 += ry2 + px - py

    # Region 2
    p2 = ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y, points)
        y -= 1
        py -= two_rx2
        if p2 > 0:
            p2 += rx2 - py
        else:
            x += 1
            px += two_ry2
            p2 += rx2 - py + px

    return points

# Main part
if __name__ == "__main__":
    xc = int(input("Enter X coordinate of center: "))
    yc = int(input("Enter Y coordinate of center: "))
    rx = int(input("Enter X radius (rx): "))
    ry = int(input("Enter Y radius (ry): "))

    ellipse_points = midpoint_ellipse(xc, yc, rx, ry)

    x_coords, y_coords = zip(*ellipse_points)

    # Plot
    plt.figure(figsize=(6,6))
    plt.plot(x_coords, y_coords, 'bo')  # blue dots
    plt.title(f"Midpoint Ellipse (center=({xc}, {yc}), rx={rx}, ry={ry})")
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.show()
