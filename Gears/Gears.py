import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_gear_vertices(teeth=12, radius=1.0, tooth_size=0.2, center=(0, 0), angle=0):
    angles = np.linspace(0, 2 * np.pi, teeth * 2, endpoint=False) + angle
    radii = np.array([radius + (tooth_size if i % 2 == 0 else 0) for i in range(len(angles))])
    x = radii * np.cos(angles) + center[0]
    y = radii * np.sin(angles) + center[1]
    return np.column_stack((x, y))

def draw_gears():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axis('off')

    gear_patches = [
        ax.add_patch(plt.Polygon(generate_gear_vertices(teeth=12, radius=1.0, tooth_size=0.2, center=(-1, 0)), fc='gray', edgecolor='black')),
        ax.add_patch(plt.Polygon(generate_gear_vertices(teeth=14, radius=1.2, tooth_size=0.2, center=(1, 0)), fc='gray', edgecolor='black')),
        ax.add_patch(plt.Polygon(generate_gear_vertices(teeth=10, radius=0.8, tooth_size=0.2, center=(0, 1.5)), fc='gray', edgecolor='black'))
    ]

    def update(frame):
        angle = frame * (np.pi / 2) / 60  # 90 degrees per second at 60 FPS
        gear_patches[0].set_xy(generate_gear_vertices(teeth=12, radius=1.0, tooth_size=0.2, center=(-1, 0), angle=angle))
        gear_patches[1].set_xy(generate_gear_vertices(teeth=14, radius=1.2, tooth_size=0.2, center=(1, 0), angle=-angle))
        gear_patches[2].set_xy(generate_gear_vertices(teeth=10, radius=0.8, tooth_size=0.2, center=(0, 1.5), angle=angle))
        return gear_patches

    ani = animation.FuncAnimation(fig, update, frames=360, interval=1000/60, blit=False)

    return fig, ani

def main():
    fig, ani = draw_gears()
    plt.show()

if __name__ == "__main__":
    main()