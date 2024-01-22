# Marching Squares Metaballs Project

## Overview

This project, implemented in February 2022, delves into the marching squares algorithm through the creation of metaballs. Three different implementations were undertaken using Python and JavaScript, leveraging the Pygame and p5.js libraries for visualization.

### Implementations

1. **Marching Squares**
   - Basic implementation of metaballs using the marching squares algorithm in both Python (Pygame) and JavaScript (p5.js).
   
2. **Without Marching Squares**
   - Implementation of metaballs without utilizing the marching squares algorithm. A comparative approach to understand the impact and efficiency of marching squares.

3. **Optimized Marching Squares**
   - Enhanced version of the marching squares implementation with optimization techniques to improve performance and rendering speed.

## Marching Squares Algorithm

The marching squares algorithm is a computational technique commonly used in computer graphics and image processing. It is particularly useful for extracting and visualizing contours from two-dimensional scalar fields.

### Basic Steps

1. **Grid Division:**
   - The 2D space is divided into a grid of cells.

2. **Thresholding:**
   - For each cell, determine the configuration of the corners based on a threshold value.

3. **Contouring:**
   - Look up a predefined set of configurations and interpolate to find the contour lines within each cell.

4. **Rendering:**
   - Draw the contours, resulting in a smooth representation of the scalar field.

## Optimizations

### 1. Lookup Table

In the basic marching squares algorithm, a lookup table is employed to determine the appropriate contour configuration based on the state of the corners. In the optimized version, this lookup table can be precomputed to avoid repeated calculations during runtime, significantly improving performance.

### 2. Interpolation Optimization

Interpolation between contour points can be computationally expensive. In the optimized marching squares, techniques such as linear interpolation or bicubic interpolation can be used to enhance the smoothness of contours while maintaining efficiency.

### 3. Data Structures

Efficient data structures can be employed to store and manipulate grid information. For example, spatial partitioning techniques like quad trees can be used to reduce the number of unnecessary calculations, especially in regions with low activity.

### 4. Parallelization

In scenarios where performance is critical, the marching squares algorithm can be parallelized to leverage multiple processing units. This can be achieved by dividing the grid into sub-regions and processing them concurrently.

## Project Structure
```
|-- python
| |-- marching_squares.py
| |-- without_marching_squares.py
| |-- optimized_marching_squares.py
|-- javascript
| |--optimized
| | |--css
| | | |-- main.css
| | |--js
| | | |-- app.js
| | | |-- balls.js
| | | |-- p5.min.js
| | |-- index.html
| |--standard
| | |--css
| | | |-- main.css
| | |--js
| | | |-- app.js
| | | |-- balls.js
| | | |-- p5.min.js
| | |-- index.html
|-- screenshots
| |-- 1.gif
| |-- 2.gif
|-- LICENSE
|-- README.md
```


## Dependencies

### Python
- Pygame library (`pip install pygame`)

### JavaScript
- p5.js library (included in the project)



## Running the Code

### Python
1. Install the required dependencies: `pip install pygame`
2. Navigate to the `python` directory.
3. Run the desired implementation:
   - `python marching_squares.py`
   - `python without_marching_squares.py`
   - `python optimized_marching_squares.py`

### JavaScript
1. Open the `index.html` file in a web browser.
2. The webpage will display the implemented metaballs using p5.js.

## Screenshots

![Screenshot 1](screenshots/1.gif)

![Screenshot 2](screenshots/2.gif)

## Conclusion

This project serves as an educational exploration of the marching squares algorithm and its application in generating metaballs. The included optimizations showcase ways to enhance performance and efficiency. Feel free to experiment, modify, and expand upon this project to deepen your understanding of marching squares and its applications.


## License

This project is licensed under the [MIT License](LICENSE).