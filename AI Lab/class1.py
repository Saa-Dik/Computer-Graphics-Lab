import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString
import numpy as np

def draw_polygon(polygon, ax):
    x, y = polygon.exterior.xy
    ax.plot(x, y, color='black')

def rectangular_fill(polygon, ax, dy=1):
    # Get bounds of the polygon
    minx, miny, maxx, maxy = polygon.bounds
    y = miny

    # Horizontal scanlines from bottom to top
    while y <= maxy:
        scanline = LineString([(minx, y), (maxx, y)])
        intersection = polygon.intersection(scanline)

        if intersection.is_empty:
            y += dy
            continue

        # Check if the result is a single line or multiple lines
        if isinstance(intersection, LineString):
            x1, y1, x2, y2 = *intersection.coords[0], *intersection.coords[-1]
            ax.plot([x1, x2], [y1, y2], color='blue')
        elif intersection.geom_type == 'MultiLineString':
            for line in intersection:
                x1, y1, x2, y2 = *line.coords[0], *line.coords[-1]
                ax.plot([x1, x2], [y1, y2], color='blue')

        y += dy

def main():
    # Define a polygon
    points = [(2, 2), (6, 3), (5, 7), (3, 6), (2, 2)]
    polygon = Polygon(points)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_title("Polygon Rectangular Filling (Horizontal Scanlines)")

    draw_polygon(polygon, ax)
    rectangular_fill(polygon, ax, dy=0.2)  # smaller dy = finer fill

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
