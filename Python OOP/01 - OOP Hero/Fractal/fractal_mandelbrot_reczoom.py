import numpy as np
import matplotlib.pyplot as plt

class MandelbrotZoom:
    def __init__(self, width=1200, height=1200, max_iter=500):
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.xmin, self.xmax = -2.0, 1.0
        self.ymin, self.ymax = -1.5, 1.5
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
        print(f"Plotting fractal with range x: [{self.xmin}, {self.xmax}], y: [{self.ymin}, {self.ymax}]")
        fractal = self.mandelbrot(self.xmin, self.xmax, self.ymin, self.ymax, 
                                  self.width, self.height, self.max_iter)
        self.ax.clear()
        self.ax.imshow(fractal, extent=[self.xmin, self.xmax, self.ymin, self.ymax],
                       cmap='inferno', origin='lower')
        self.ax.set_title("Mandelbrot Set (Zoomable)")
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
                if abs(x1 - x0) > 1e-6 and abs(y1 - y0) > 1e-6:
                    self.xmin, self.xmax = sorted([x0, x1])
                    self.ymin, self.ymax = sorted([y0, y1])
                    self.plot_fractal()
                else:
                    print("Selected area too small to zoom!")
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

# Run the Mandelbrot zoomable fractal
MandelbrotZoom()
