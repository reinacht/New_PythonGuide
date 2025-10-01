import numpy as np
import matplotlib.pyplot as plt

class JuliaSetZoom:
    def __init__(self, c=-0.7 + 0.27015j, width=800, height=800, max_iter=300):
        self.c = c  # Parameter konstanta kompleks
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.xmin, self.xmax = -1.5, 1.5  # Rentang awal untuk sumbu x
        self.ymin, self.ymax = -1.5, 1.5  # Rentang awal untuk sumbu y
        self.fig, self.ax = plt.subplots()
        self.rect = None
        self.start = None
        self.end = None
        self.zooming = False

        self.plot_fractal()
        self.fig.canvas.mpl_connect("button_press_event", self.on_press)
        self.fig.canvas.mpl_connect("button_release_event", self.on_release)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_motion)
        plt.show()

    def generate(self):
        # Buat grid untuk sumbu x dan y
        x = np.linspace(self.xmin, self.xmax, self.width)
        y = np.linspace(self.ymin, self.ymax, self.height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y  # Bilangan kompleks untuk setiap koordinat

        # Array untuk menyimpan iterasi
        iteration_counts = np.zeros(Z.shape, dtype=int)

        # Iterasi Julia Set
        for i in range(self.max_iter):
            mask = np.abs(Z) <= 2  # Masking untuk nilai |Z| <= 2
            Z[mask] = Z[mask]**2 + self.c  # Update Z
            iteration_counts[mask & (np.abs(Z) > 2)] = i  # Simpan iterasi di mana |Z| > 2

        return iteration_counts

    def plot_fractal(self):
        fractal = self.generate()
        self.ax.clear()
        self.ax.imshow(fractal, extent=[self.xmin, self.xmax, self.ymin, self.ymax],
                       cmap='inferno', origin='lower')
        self.ax.set_title(f"Julia Set (c={self.c})")
        self.ax.set_xlabel("Re")
        self.ax.set_ylabel("Im")
        plt.draw()

    def on_press(self, event):
        if event.inaxes is not None:
            self.start = (event.xdata, event.ydata)
            self.rect = plt.Rectangle(self.start, 0, 0, edgecolor='white', fill=False)
            self.ax.add_patch(self.rect)
            self.zooming = True

    def on_release(self, event):
        if self.zooming and event.inaxes is not None:
            self.end = (event.xdata, event.ydata)
            self.zooming = False
            if self.start and self.end:
                x0, y0 = self.start
                x1, y1 = self.end
                self.xmin, self.xmax = sorted([x0, x1])
                self.ymin, self.ymax = sorted([y0, y1])
                self.plot_fractal()
            self.rect = None
            self.start = None
            self.end = None

    def on_motion(self, event):
        if self.zooming and event.inaxes is not None:
            x0, y0 = self.start
            x1, y1 = event.xdata, event.ydata
            width = x1 - x0
            height = y1 - y0
            self.rect.set_width(width)
            self.rect.set_height(height)
            self.rect.set_xy((x0, y0))
            plt.draw()

# Jalankan Julia Set dengan fitur zoom
JuliaSetZoom(c=-0.8 + 0.156j)
