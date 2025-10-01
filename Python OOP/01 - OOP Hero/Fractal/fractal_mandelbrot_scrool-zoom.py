import numpy as np
import matplotlib.pyplot as plt

class MandelbrotZoomScroll:
    def __init__(self, width=800, height=800, max_iter=200):
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.xmin, self.xmax = -2.0, 1.0
        self.ymin, self.ymax = -1.5, 1.5
        self.zoom_factor = 0.8  # Faktor zoom (80% untuk zoom in, 125% untuk zoom out)
        self.fig, self.ax = plt.subplots()

        self.plot_fractal()
        self.fig.canvas.mpl_connect("scroll_event", self.on_scroll)
        plt.show()

    def mandelbrot(self, xmin, xmax, ymin, ymax, width, height, max_iter):
        x = np.linspace(xmin, xmax, width)
        y = np.linspace(ymin, ymax, height)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        Z = np.zeros_like(C)
        M = np.full(C.shape, max_iter, dtype=int)

        for i in range(max_iter):
            mask = np.abs(Z) <= 2
            Z[mask] = Z[mask]**2 + C[mask]
            M[mask & (np.abs(Z) > 2)] = i

        return M

    def plot_fractal(self):
        fractal = self.mandelbrot(self.xmin, self.xmax, self.ymin, self.ymax, 
                                  self.width, self.height, self.max_iter)
        self.ax.clear()
        self.ax.imshow(fractal, extent=[self.xmin, self.xmax, self.ymin, self.ymax],
                       cmap='inferno', origin='lower')
        self.ax.set_title("Mandelbrot Set (Scroll to Zoom)")
        self.ax.set_xlabel("Re")
        self.ax.set_ylabel("Im")
        plt.draw()

    def on_scroll(self, event):
        # Dapatkan posisi mouse saat ini
        x_center = event.xdata
        y_center = event.ydata

        if x_center is None or y_center is None:
            return  # Jika posisi di luar plot, abaikan

        # Zoom in atau out
        if event.button == 'up':  # Zoom in
            scale = self.zoom_factor
        elif event.button == 'down':  # Zoom out
            scale = 1 / self.zoom_factor
        else:
            return

        # Update range berdasarkan posisi scroll
        x_range = (self.xmax - self.xmin) * scale
        y_range = (self.ymax - self.ymin) * scale

        self.xmin = x_center - x_range / 2
        self.xmax = x_center + x_range / 2
        self.ymin = y_center - y_range / 2
        self.ymax = y_center + y_range / 2

        # Tampilkan ulang fraktal
        self.plot_fractal()

# Jalankan program Mandelbrot dengan zoom scroll
MandelbrotZoomScroll()
